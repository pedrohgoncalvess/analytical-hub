from fastapi import FastAPI, File, UploadFile, status, HTTPException
import duckdb
import io
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
import os
from database.models.file.file import File as FileSchema
from database.connection import DatabaseConnection
from database.query.file.file import FileQuery
from utils.local_exception import LocalException

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/upload/file")
async def post_file(file: UploadFile = File(...), separator: str = ','):
    fileContent = await file.read()
    fileContentStr = fileContent.decode('utf-8')
    fileName = file.filename.split(".")[0].lower().replace(" ", "_")
    fileExtension = file.filename.split(".")[1].lower()
    fileContentIo = io.StringIO(fileContentStr)

    main = duckdb.read_csv(fileContentIo, sep=separator)
    duckdb.sql(f"copy main to 's3/{file.filename}'")

    path = "s3/"
    files = os.listdir(path)
    filesSizes = {file: f"{os.path.getsize(os.path.join(path, file)) / (1024 * 1024):.2f}" for file in files}

    rowsNumber = duckdb.sql("SELECT COUNT(*) FROM main").fetchdf().iloc[0, 0]
    dfColumns = list(duckdb.sql("SELECT * FROM main limit 1").to_df().columns)
    fileSize = filesSizes.get(file.filename)

    dbConnection = DatabaseConnection()
    newFile = FileSchema(name=fileName,
                         type=fileExtension,
                         size=float(fileSize),
                         nb_columns=len(dfColumns),
                         nb_rows=int(rowsNumber)
                         )

    schemaInfo = duckdb.sql(f"DESCRIBE TABLE main").to_df()

    insertFileResult = dbConnection.addNewObject(newFile)
    if isinstance(insertFileResult, LocalException):
        raise HTTPException(insertFileResult.status_code, insertFileResult.error_message)

    fileQuery = FileQuery()
    fileId = fileQuery.getFileByName(fileName).id


    schemaInfoList = []
    for column in dfColumns:
        rowOfDfSchema = schemaInfo[schemaInfo['column_name'] == column]
        columnType = rowOfDfSchema['column_type'].iloc[0]
        hvNull = True if rowOfDfSchema['null'].iloc[0] == 'YES' else False
        hvDefault = rowOfDfSchema['default'].iloc[0]
        schemaInfoList.append({"id_table": fileId, "column_name": column, "column_type": columnType, "null": hvNull,
                               "default": hvDefault})
        print(schemaInfoList)
    schemaInsert = fileQuery.bulkInsertSchema(schemaInfoList)
    if isinstance(schemaInsert, LocalException):
        fileQuery.deleteFileByName(fileId)
        raise HTTPException(schemaInsert.status_code, schemaInsert.error_message)

    return status.HTTP_201_CREATED


@app.get("/file/schema")
async def get_schema(id: int):
    fileQuery = FileQuery()
    return {"schema": fileQuery.getSchemaByIdFile(id)}


@app.get("/file/list")
async def get_file_list():
    fileQuerys = FileQuery()

    return {"files": fileQuerys.getAllFiles()}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info", reload=True)
