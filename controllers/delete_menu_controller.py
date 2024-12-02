from utils.response import response
from services.menus import delete_menu

def delete_menu_controller(id):
    return response(delete_menu(id))