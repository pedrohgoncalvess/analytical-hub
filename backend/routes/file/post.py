import io
import duckdb
from database.operations.file import FileQuery
from fastapi import APIRouter, File, UploadFile, status, HTTPException
from database.models.file.file import File as FileSchema

router = APIRouter(
    prefix='/file',
    tags=['file'],
    responses={404: {"description": "Not found"}},
)


@router.post('/preview', status_code=201)
async def file_preview(file: UploadFile = File(...), separator: str = ',', header: bool = True):
    fileContent = file.file.read()
    try:
        fileContentStr = fileContent.decode('utf-8')
    except UnicodeDecodeError:
        fileContentStr = fileContent.decode('ISO-8859-1')
    fileContentIo = io.StringIO(fileContentStr)

    main = duckdb.read_csv(fileContentIo, sep=separator, header=header)
    view = duckdb.sql("select * from main limit 5").to_df().to_dict(orient='records')

    return view


@router.post('/upload', status_code=201)
async def post_file(file: UploadFile = File(...), separator: str = ',', header: bool = True):
    import os
    fileQuery = FileQuery()

    fileName = file.filename.split(".")[0].lower().replace(" ", "_")
    fileExtension = file.filename.split(".")[1].lower()

    if fileQuery.object_exists(fileName, fileExtension):
        raise HTTPException(status_code=409, detail="File already exists.")

    fileContent = file.file.read()

    try:
        fileContentStr = fileContent.decode('utf-8')
    except UnicodeDecodeError:
        fileContentStr = fileContent.decode('ISO-8859-1')
    fileContentIo = io.StringIO(fileContentStr)

    main = duckdb.read_csv(fileContentIo, sep=separator, header=header)
    duckdb.sql(f"copy main to 's3/{file.filename}'")

    path = "s3/"
    files = os.listdir(path)
    filesSizes = {file: f"{os.path.getsize(os.path.join(path, file)) / (1024 * 1024):.2f}" for file in files}

    rowsNumber = duckdb.sql("SELECT COUNT(*) FROM main").fetchdf().iloc[0, 0]
    dfColumns = list(duckdb.sql("SELECT * FROM main limit 1").to_df().columns)
    fileSize = filesSizes.get(file.filename)

    insertFileResult = fileQuery.add_new_file(
                    FileSchema(
                        name=fileName,
                        type=fileExtension,
                        size=float(fileSize),
                        nb_columns=len(dfColumns),
                        nb_rows=int(rowsNumber)
                             )
                    )
    if insertFileResult.error:
        raise HTTPException(insertFileResult.status_code, insertFileResult.message)

    fileId = fileQuery.get_file_by_name(fileName).id

    schemaInfo = duckdb.sql(f"DESCRIBE TABLE main").to_df()

    schemaInfoList = []
    for column in dfColumns:
        rowOfDfSchema = schemaInfo[schemaInfo['column_name'] == column]
        columnType = rowOfDfSchema['column_type'].iloc[0]
        hvNull = True if rowOfDfSchema['null'].iloc[0] == 'YES' else False
        hvDefault = rowOfDfSchema['default'].iloc[0]
        schemaInfoList.append({"id_table": fileId, "column_name": column,
                               "column_type": columnType, "null": hvNull,
                               "default": hvDefault})

    schemaInsertResult = fileQuery.bulk_insert_schema(schemaInfoList)
    if schemaInsertResult.error:
        fileQuery.delete_file_by_id(fileId)
        raise HTTPException(schemaInsertResult.status_code, schemaInsertResult.message)

    return status.HTTP_201_CREATED
