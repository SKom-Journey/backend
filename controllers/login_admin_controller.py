from utils.response import response
from services.admins import admin_by_username
from bcrypt import checkpw
from models.Admin import Admin
from services.sessions import create_session, UserType

def login_admin_controller(json: dict):
    admin = admin_by_username(json['username'])
    if admin == None:
        return response("Username Not Found", "ERROR", True)
    
    if checkpw(json['password'].encode(), admin['password'].encode()):
        session = create_session(user_id=admin['id'], type=UserType.ADMIN)
        return response(Admin(
            session=session,
            password=admin['password'],
            username=admin['username'],
            created_at=admin['created_at'].isoformat(),
        ).model_dump())
    else:
        return response("Password Incorrect", "ERROR", True)