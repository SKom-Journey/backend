from flask import Response
from models.Session import Session

def set_session(response: Response, session: Session):
    response.set_cookie(
        key="Ryomu_AccessToken",
        value=session['access_token'],
        httponly=True,
        secure=True,
        samesite="None",
        path="/",
        max_age=604800
    )
    response.set_cookie(
        key="Ryomu_RefreshToken",
        value=session['id'],
        httponly=True,
        secure=True,
        samesite="None",
        path="/",
        max_age=604800
    )