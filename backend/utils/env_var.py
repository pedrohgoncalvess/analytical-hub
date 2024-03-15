from dotenv import load_dotenv
import os

if os.path.isfile('.env'):
    load_dotenv('.env')
else:
    load_dotenv(".env.docker")


def get_env_var(var: str) -> str:
    return os.getenv(var)
