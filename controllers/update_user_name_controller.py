from utils.response import response
from services.users import update_user_name

def update_user_name_controller(id: str, json: dict):
    return response(update_user_name(id, json['name']))