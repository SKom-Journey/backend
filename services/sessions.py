from utils.mongodb import db
from models.Session import Session, UserType
from datetime import datetime, timedelta, timezone
from bson import ObjectId
from configs.config import SESSION_SECRET, SESSION_ADMIN_SECRET
import jwt

tb_name = 'sessions'

def create_session(user_id: str, type: UserType):
    secret = SESSION_SECRET if type.value == 'USER' else SESSION_ADMIN_SECRET
    session_id = db.get_collection(tb_name).insert_one({"type": type.value, "user_id": ObjectId(user_id), "created_at": datetime.now()}).inserted_id
    session = db.get_collection(tb_name).find_one({"_id": ObjectId(session_id)})
    access_token = jwt.encode({
        'user_id': user_id,
        'exp': datetime.now(timezone.utc) + timedelta(minutes=15)
    }, secret, algorithm='HS256')
    return Session(
        access_token=access_token,
        id=str(session['_id']),
        user_id=user_id,
        type=type.value,
        created_at = session['created_at'].isoformat(),
    ).model_dump()