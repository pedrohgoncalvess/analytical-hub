from sqlalchemy import select
from database.connection import DatabaseConnection
from database.models.file.file import File
from sqlalchemy import insert, delete

from database.models.file.schema import Schema
from utils.local_exception import LocalException


class FileQuery(DatabaseConnection):
    def getAllFiles(self):
        session = self.__newSession__()
        results = session.scalars(select(File)).all()
        session.close()
        return results

    def getFileByName(self, name: str):
        session = self.__newSession__()
        results = session.scalars(select(File).where(File.name == name)).first()
        session.close()
        return results

    def bulkInsertSchema(self, schema: list[dict:str:any]):
        session = self.__newSession__()
        global valueReturn
        try:
            session.execute(insert(Schema), schema)
            session.commit()
            valueReturn = True
        except Exception as e:
            valueReturn = LocalException()
        finally:
            session.close()
            return valueReturn

    def deleteFileByName(self, id: int):
        session = self.__newSession__()
        global valueReturn
        try:
            stmt = delete(File).where(File.id == id)
            session.execute(stmt)
            session.commit()
            valueReturn = True
        except Exception:
            valueReturn = LocalException()
        finally:
            session.close()
            return valueReturn

    def getSchemaByIdFile(self, id: int):
        session = self.__newSession__()
        results = session.scalars(select(Schema).where(Schema.id_table == id)).all()
        session.close()
        return results
