from utils.response import response
from services.menus import menus_by_not_in_ids
from services.menu_categories import get_menu_category_by_category_id

def get_menus_not_in_category_controller(category_id: str):
    menu_ids = []
    for menu_categories in get_menu_category_by_category_id(category_id):
        menu_ids.append(menu_categories['menu_id'])
    return response(menus_by_not_in_ids(menu_ids), "SUCCESS", False)