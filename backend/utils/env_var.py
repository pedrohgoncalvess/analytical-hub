from dotenv import load_dotenv
import os
from utils.configs import get_root_directory

rootDir = get_root_directory()

if os.path.isfile(f'{rootDir}\\.env'):
    load_dotenv(f'{rootDir}\\.env')
else:
    load_dotenv(f'{rootDir}\\.env.docker')


def get_env_var(var: str) -> str:
    return os.getenv(var)
