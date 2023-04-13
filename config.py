import os
from dotenv import load_dotenv

load_dotenv()


def get_env_variable(name, default=None):
    try:
        return os.environ[name]
    except KeyError:
        return default


MONGO_DB_HOST = get_env_variable("MONGO_DB_HOST", default="localhost")
MONGO_DB_PORT = get_env_variable("MONGO_DB_PORT", default=27017)
MONGO_DB_NAME = get_env_variable("MONGO_DB_NAME")
MONGO_DB_USER = get_env_variable("MONGO_DB_USER")
MONGO_DB_PASSWORD = get_env_variable("MONGO_DB_PASSWORD", default="root")
