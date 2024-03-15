from fastapi import APIRouter
from database.operations.file import FileQuery

router = APIRouter(
    prefix='/file',
    tags=['file'],
    responses={404: {"description": "Not found"}},
)

@router.get("/schema")
async def get_schema(id: int):
    fileQuery = FileQuery()
    return {"schema": fileQuery.get_schema_by_id_file(id)}


@router.get("/list")
async def get_file_list():
    fileQuerys = FileQuery()

    return {"files": fileQuerys.get_all_files()}