from utils.response import response
from services.users import create_user, user_by_email
from services.oauth import get_google_info
from services.sessions import create_session, UserType
from models.User import User

def register_oauth_user_controller(access_token: str):
    user = get_google_info(access_token)
    check_email_exist = user_by_email(user['email'])
    if check_email_exist == None:
        return response(create_user(
            user['email'],
            user['email'],
            user['name'],
            True,
            True
        ))
    
    session = create_session(user_id=check_email_exist['id'], type=UserType.USER)
    return response(User(
        session=session,
        id=check_email_exist['id'],
        email=check_email_exist['email'],
        password=check_email_exist['password'],
        name=check_email_exist['name'],
        with_google=check_email_exist['with_google'],
        created_at=check_email_exist['created_at'],
    ).model_dump())