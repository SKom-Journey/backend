from utils.response import response
from services.admins import admin_by_username
from bcrypt import checkpw
from models.Admin import Admin
from services.sessions import create_session, UserType
from flask import make_response
from utils.set_session import set_session

def login_admin_controller(json: dict):
    admin = admin_by_username(json['username'])
    if admin == None:
        return response("Username Not Found", "ERROR", True)
    
    if checkpw(json['password'].encode(), admin['password'].encode()):
        session = create_session(user_id=admin['id'], type=UserType.ADMIN)
        res = make_response(response(Admin(
            id=admin['id'],
            password=admin['password'],
            username=admin['username'],
            created_at=admin['created_at'],
        ).model_dump()))
        set_session(res, session)
        return res
    else:
        return response("Password Incorrect", "ERROR", True)