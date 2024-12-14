from utils.response import response
from services.users import user_by_id

def get_profile_controller(payload):
    return response(user_by_id(payload['user_id']))