from utils.response import response
from services.menus import delete_menu, menu_by_id
from utils.delete_file import delete_file

def delete_menu_controller(id):
    menu = menu_by_id(id)
    if menu:
        delete_file(menu['img'])
    return response(delete_menu(id))