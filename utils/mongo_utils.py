from database import db

def save_user(user_data):
    users_collection = db.get_collection("users")
    users_collection.insert_one(user_data)

def get_user(user_id):
    users_collection = db.get_collection("users")
    return users_collection.find_one({"user_id": user_id})
