from utils.response import response
from services.menus import menu_by_id

def get_menu_controller(id: str):
    return response(menu_by_id(id))