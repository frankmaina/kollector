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
MONGO_DB_NAME = get_env_variable("MONGO_DB_NAME", default="test")
MONGO_DB_USER = get_env_variable("MONGO_DB_USER",  default="user")
MONGO_DB_PASSWORD = get_env_variable("MONGO_DB_PASSWORD", default="root") # you definitely should specify a more secure password for production
WORKING_ENV =  get_env_variable("WORKING_ENV", default="development")
