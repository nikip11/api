from bson import ObjectId
from app.core.db import db_client
from .models import User
from .schemas import user_schema

def find_user(field: str, key):
    try:
        user = db_client.users.find_one({field: key})
        user = db_client.users.find_one({field: key})
        return User(**user) if user else None
        # return User(**user_schema(user))
    except:
        return {"error": "No se ha encontrado el usuario"}

def save_user(user: User):
    user_dict = dict(user)
    del user_dict["id"]
    id = db_client.users.insert_one(user_dict).inserted_id
    return user_schema(db_client.users.find_one({"_id": ObjectId(id)}))