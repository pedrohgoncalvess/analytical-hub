import sqlalchemy
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker, Session
from starlette import status
from utils.configs import get_env_var
from utils.local_exception import LocalException


class DatabaseConnection:
    def __init__(self):
        self.__dbHost__ = get_env_var("DB_HOST")
        self.__dbPort__ = get_env_var("DB_PORT")
        self.__dbName_ = get_env_var("DB_NAME")
        self.__dbUser__ = get_env_var("DB_USER")
        self.__dbPassword__ = get_env_var("DB_PASSWORD")

        self._engine_ = create_engine(
            f"postgresql+psycopg2://{self.__dbUser__}:{self.__dbPassword__}@{self.__dbHost__}:{self.__dbPort__}/{self.__dbName_}")
        self.schemas = ['file']

    def __newSession__(self) -> Session:
        return sessionmaker(autocommit=False, autoflush=False, bind=self._engine_, expire_on_commit=False)()

    def addNewObject(self, newObject):
        session = self.__newSession__()
        global valueReturn
        try:
            session.add(newObject)
            session.commit()
            valueReturn = True
        except sqlalchemy.exc.IntegrityError:
            valueReturn = LocalException("Duplicate object", status_code=status.HTTP_409_CONFLICT)
        except Exception:
            valueReturn = LocalException()
        finally:
            session.close()
            return valueReturn
