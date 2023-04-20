import pymongo
from config import (
    MONGO_DB_HOST,
    MONGO_DB_NAME,
    MONGO_DB_PASSWORD,
    MONGO_DB_PORT,
    MONGO_DB_USER,
    WORKING_ENV,
)

_db = None


def connect_to_mongodb():
    uri = f"mongodb://{MONGO_DB_USER}:{MONGO_DB_PASSWORD}@{MONGO_DB_HOST}:{MONGO_DB_PORT}/"
    try:
        client = pymongo.MongoClient(uri, serverSelectionTimeoutMS=2000)
        # if not WORKING_ENV == "test":
        #     client.admin.command("ismaster")
    except pymongo.errors.ConnectionFailure as e:
        raise Exception("Could not connect to MongoDB: %s" % e)
    except pymongo.errors.ServerSelectionTimeoutError as e:
        raise Exception("Could not connect to MongoDB: %s" % e)
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
