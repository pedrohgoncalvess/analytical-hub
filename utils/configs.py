from dotenv import load_dotenv
import os

load_dotenv()


def get_env_var(var: str) -> str:
    return os.getenv(var)
