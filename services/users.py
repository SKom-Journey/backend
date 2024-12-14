from utils.mongodb import db
from bson import ObjectId
from models.User import User
from datetime import datetime
import bcrypt
from services.sessions import create_session

tb_name = 'users'

def create_user(email: str, password: str, name: str, with_google: bool):
    salt = bcrypt.gensalt()
    hashed_password = None if len(password) == 0 else bcrypt.hashpw(password.encode(), salt)
    user_id = db.get_collection(tb_name).insert_one({"email": email, "password": hashed_password, "name": name, "with_google": with_google, "created_at": datetime.now()}).inserted_id
    user = db.get_collection(tb_name).find_one({"_id": ObjectId(user_id)})

    return User(
        id=str(user['_id']),
        email=user['email'],
        password=user['password'],
        name=user['name'],
        with_google=user['with_google'],
        created_at=user['created_at'].isoformat(),
    ).model_dump() 

def user_by_id(id: str):
    user = db.get_collection(tb_name).find_one({"_id": ObjectId(id)})
    if user != None:
        return User(
            id=str(user['_id']),
            email=user['email'],
            password=user['password'],
            name=user['name'],
            with_google=user['with_google'],
            created_at=user['created_at'].isoformat(),
        ).model_dump() 
    return None

def delete_user_by_id(id: str):
    delete = db.get_collection(tb_name).delete_one({"_id": ObjectId(id)})
    return delete.deleted_count

def user_by_email(email: str):
    user = db.get_collection(tb_name).find_one({"email": email})
    if user != None:
        return User(
            id=str(user['_id']),
            email=user['email'],
            password=user['password'],
            name=user['name'],
            with_google=user['with_google'],
            created_at=user['created_at'].isoformat(),
        ).model_dump() 
    
    return None