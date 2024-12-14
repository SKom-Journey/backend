from functools import wraps
from utils.response import response
from jwt import ExpiredSignatureError, decode, InvalidTokenError
from flask import request
from configs.config import SESSION_SECRET, CORS_ALLOWED_ORIGINS

def check_user_jwt(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.cookies.get('Ryomu_AccessToken')
        if not token:
            return response(None, 'INVALID_TOKEN')
        try:
            decoded_token = decode(token, SESSION_SECRET, algorithms=["HS256"])
            payload = decoded_token
        except ExpiredSignatureError:
            return response(None, 'TOKEN_EXPIRED')
        except InvalidTokenError:
            return response(None, 'INVALID_TOKEN')
        return f(payload, *args, **kwargs)
    return decorated_function