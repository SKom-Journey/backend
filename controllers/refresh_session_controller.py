from utils.response import response
from utils.set_session import set_session
from services.sessions import refresh_session
from flask import make_response

def refresh_session_controller(refresh_token: str):
    session = refresh_session(refresh_token)
    res = make_response(response(session))
    set_session(res, session)
    return res