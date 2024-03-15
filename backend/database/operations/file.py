from sqlalchemy import select
from database.settings import DatabaseConnection
from database.models.file.file import File
from sqlalchemy import insert, delete
from database.models.file.schema import Schema
from database.operations.operations_manager import OperationsManager


class FileQuery(DatabaseConnection):
    def add_new_file(self, file: File) -> OperationsManager:
        with self as session:
            try:
                session.add(file)
                session.commit()
                return OperationsManager()
            except Exception as error:
                return OperationsManager(error=True, message=error)

    def object_exists(self, name: str, _type: str) -> bool:
        with self as session:
            result = session.scalars(select(File).where(File.name == name).where(File.type == _type)).first()
        if result:
            return True
        else:
            return False

    def get_all_files(self) -> list[File]:
        with self as session:
            results = session.scalars(select(File)).all()
            return results

    def get_file_by_name(self, name: str) -> File:
        with self as session:
            result = session.scalars(select(File).where(File.name == name)).first()
            return result

    def bulk_insert_schema(self, schema: list[dict:str:any]) -> OperationsManager:
        with self as session:
            try:
                session.execute(insert(Schema), schema)
                session.commit()
                return OperationsManager()
            except Exception as error:
                return OperationsManager(error=True, message=error)

    def delete_file_by_id(self, _id: int):
        with self as session:
            try:
                stmt = delete(File).where(File.id == _id)
                session.execute(stmt)
                session.commit()
                return OperationsManager()
            except Exception as error:
                return OperationsManager(error=True, message=error)

    def get_schema_by_id_file(self, _id: int):
        with self as session:
            results = session.scalars(select(Schema).where(Schema.id_table == _id)).all()
            return results
