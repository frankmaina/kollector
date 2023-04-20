import pymongo
from pymongo.errors import ServerSelectionTimeoutError

from config import (
    MONGO_DB_HOST,
    MONGO_DB_NAME,
    MONGO_DB_PASSWORD,
    MONGO_DB_PORT,
    MONGO_DB_USER,
)

_db = None


def connect_to_mongodb():
    uri = "mongodb://{}:{}@{}:{}/".format(
        MONGO_DB_USER, MONGO_DB_PASSWORD, MONGO_DB_HOST, MONGO_DB_PORT
    )
    try:
        client = pymongo.MongoClient(uri, serverSelectionTimeoutMS=2000)
        # if not WORKING_ENV == "test":
        #     client.admin.command("ismaster")
    except ServerSelectionTimeoutError as e:
        raise e
    db = client[MONGO_DB_NAME]
    return db


def get_schema_collection():
    global _db
    if _db is None:
        _db = connect_to_mongodb()
    return _db["formSchemas"]


def get_form_collection():
    global _db
    if _db is None:
        _db = connect_to_mongodb()
    return _db["forms"]
