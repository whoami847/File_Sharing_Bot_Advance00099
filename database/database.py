import pymongo
from config import DATABASE_URL

client = pymongo.MongoClient(DATABASE_URL)
db = client.get_database()

# Example: Getting the collection of files
files_collection = db.get_collection("files")
