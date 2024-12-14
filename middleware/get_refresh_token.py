from functools import wraps
from utils.response import response
from flask import request

def get_refresh_token(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.cookies.get('Ryomu_RefreshToken')
        if not token:
            return response(None, 'INVALID_TOKEN')
        return f(token, *args, **kwargs)
    return decorated_function