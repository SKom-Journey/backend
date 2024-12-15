from utils.response import response
from services.menus import menu_by_id
from services.menu_categories import get_menu_category_by_category_id

def get_menus_by_category_controller(category_id: str):
    result = []
    for menu_categories in get_menu_category_by_category_id(category_id):
        menu = menu_by_id(menu_categories['menu_id'])
        result.append(menu)
    return response(result, "SUCCESS", False)