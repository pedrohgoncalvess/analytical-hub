from fastapi import FastAPI, File, UploadFile, status, HTTPException
import duckdb
import io
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
import os

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
    try:
        file_content = await file.read()
        file_content_str = file_content.decode('utf-8')

        file_content_io = io.StringIO(file_content_str)

        main = duckdb.read_csv(file_content_io, sep=separator)
        duckdb.sql(f"copy main to 's3/{file.filename.split('.')[0]}.parquet'")

        return status.HTTP_201_CREATED
    except Exception as e:
        print(f"Erro no servidor: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro interno no servidor")


@app.get("/file/schema")
async def get_schema(path: str):
    if not path.endswith('.parquet'):
        path += '.parquet'

    path = "s3/"+path.replace('-','/')
    df = duckdb.sql(f"select * from '{path}' limit 1").df()
    schema = [{"name": column, "type": str(col_type)} for column, col_type in list(df.dtypes.items())]
    return {"columns": schema}



@app.get("/file/list")
async def get_file_list(path:str=""):
    if path == "":
        path = "s3/"
    files = os.listdir(path)

    newFiles = [file for file in files if os.path.isfile(os.path.join(path, file))]
    filesSizes = [{"file":file,"size": f"{os.path.getsize(os.path.join(path, file)) / (1024 * 1024):.2f} mb"} for file in newFiles]

    return {"files": filesSizes}


if __name__ == "__main__":
    uvicorn.run("main:app", port=9000, log_level="info", reload=True)