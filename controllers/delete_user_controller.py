from utils.response import response
from services.users import delete_user_by_id

def delete_user_controller(id: str):
    return response(delete_user_by_id(id))