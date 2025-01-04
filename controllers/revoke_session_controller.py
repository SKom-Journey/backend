from utils.response import response
from services.sessions import get_and_delete_session

def revoke_session_controller(refresh_token: str):
    session = get_and_delete_session(refresh_token)
    return response(session)