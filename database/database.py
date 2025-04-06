import pymongo
from config import MONGO_URI

def get_db_connection():
    client = pymongo.MongoClient(MONGO_URI)
    db = client.get_database()
    return db
