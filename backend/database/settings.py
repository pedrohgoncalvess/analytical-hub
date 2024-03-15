from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from utils.env_var import get_env_var
import os
from utils.env_var import rootDir


class DatabaseConnection:
    def __init__(self):
        self.__dbHost__ = get_env_var("DB_HOST")
        self.__dbPort__ = get_env_var("DB_PORT")
        self.__dbName_ = get_env_var("DB_NAME")
        self.__dbUser__ = get_env_var("DB_USER")
        self.__dbPassword__ = get_env_var("DB_PASSWORD")

        self._engine_ = create_engine(
            f"postgresql+psycopg2://{self.__dbUser__}:{self.__dbPassword__}@{self.__dbHost__}:{self.__dbPort__}/{self.__dbName_}"
        )

        self.schemas = [schemaName for schemaName in os.listdir(f"{rootDir}\\database\\models\\") if
                        os.path.isdir(os.path.join(f"{rootDir}\\database\\models\\", schemaName))]

        def buildSchemas(schemas: list[str]) -> None:
            for schema in schemas:
                dbConn = sessionmaker(autocommit=False, autoflush=False, bind=self._engine_, expire_on_commit=False)()
                dbConn.execute(text(f"CREATE SCHEMA IF NOT EXISTS {schema}"))
                dbConn.commit()
                dbConn.close()

        buildSchemas(self.schemas)

    def __enter__(self):
        self.dbConn = sessionmaker(autocommit=False, autoflush=False, bind=self._engine_, expire_on_commit=False)()
        return self.dbConn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.dbConn.close()


dbConnection = DatabaseConnection()
