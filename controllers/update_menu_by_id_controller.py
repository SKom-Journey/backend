from utils.response import response
from services.menus import update_menu_by_id

def update_menu_by_id_controller(id: str, menu: dict):
    return response(update_menu_by_id(id, menu))