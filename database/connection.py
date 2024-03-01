from utils.configs import get_env_var


class DatabaseConnection:
    def __init__(self):
        self.dbHost = get_env_var("DB_HOST")
        self.dbPort = get_env_var("DB_PORT")
        self.dbName = get_env_var("DB_NAME")
        self.dbUser = get_env_var("DB_USER")
        self.dbPassword = get_env_var("DB_PASSWORD")
