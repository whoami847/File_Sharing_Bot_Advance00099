import pymongo
from config import MONGO_URI

# Initialize MongoDB connection
client = pymongo.MongoClient(MONGO_URI)
db = client.get_database()

# Add a file record to MongoDB
def add_file_record(file_id, file_name):
    files_collection = db.files
    files_collection.insert_one({"file_id": file_id, "file_name": file_name})
