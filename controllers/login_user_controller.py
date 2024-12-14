from utils.response import response
from services.users import user_by_email
from services.sessions import create_session
from models.Session import UserType
from bcrypt import checkpw
from models.User import User
from flask import make_response
from utils.set_session import set_session

def login_user_controller(json: dict):
    user = user_by_email(json['email'])
    if user == None:
        return response("Email Not Found", "ERROR", True)
    
    if checkpw(json['password'].encode(), user['password'].encode()):
        session = create_session(user_id=user['id'], type=UserType.USER)
        res = make_response(response(User(
            id=user['id'],
            email=user['email'],
            password=user['password'],
            name=user['name'],
            with_google=user['with_google'],
            created_at=user['created_at'],
        ).model_dump()))
        set_session(res, session)
        return res
    else:
        return response("Password Incorrect", "ERROR", True)