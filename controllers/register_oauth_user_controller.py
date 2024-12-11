from utils.response import response
from services.users import create_user, user_by_email
from services.oauth import get_google_info

def register_oauth_user_controller(access_token: str):
    user = get_google_info(access_token)
    checkEmailExist = user_by_email(user['email'])
    if checkEmailExist == None:
        return response(create_user(
            user['email'],
            user['email'],
            user['name'],
            True
        ))
    
    return response("Email Already Exist", "ERROR", True)