from utils.response import response
from services.menus import menu_by_id, menus

def get_menu_controller(id: str):
    if id == 'all':
        return response(menus(''))
    return response(menu_by_id(id))