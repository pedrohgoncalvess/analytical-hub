from fastapi import FastAPI, File, UploadFile, status
import duckdb
import io

app = FastAPI()


@app.post("/upload/file")
async def post_file(file: UploadFile = File(...), separator: str = ','):
    file_content = await file.read()
    file_content_str = file_content.decode('utf-8')

    file_content_io = io.StringIO(file_content_str)

    main = duckdb.read_csv(file_content_io, sep=separator)
    duckdb.sql(f"copy main to 's3/{file.filename.split('.')[0]}.parquet'")

    return status.HTTP_201_CREATED


@app.get("/file/schema")
async def get_schema(path: str):
    if not path.endswith('.parquet'):
        path += '.parquet'

    path = "s3/"+path.replace('-','/')
    df = duckdb.sql(f"select * from '{path}' limit 1").df()
    schema = [{"name": column, "type": str(col_type)} for column, col_type in list(df.dtypes.items())]
    return {"columns": schema}
