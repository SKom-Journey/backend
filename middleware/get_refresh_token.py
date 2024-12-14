from functools import wraps
from utils.response import response
from flask import request

def get_refresh_token(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        refresh_token = request.cookies.get('Ryomu_RefreshToken')
        if not refresh_token:
            return response(None, 'INVALID_TOKEN')
        return f(refresh_token, *args, **kwargs)
    return decorated_function