from utils.response import response
from services.menus import menus_by_ids, menus_by_not_in_ids, menus
from services.categories import get_categories
from models.Menu import MenuList
from services.menu_categories import get_menu_category_by_category_id

def get_menus_controller(keyword: str):
    if keyword:
        return response(menus(keyword))
    
    result = []
    stored_menu_ids = []
    
    for category in get_categories():
        menu_ids = []
        for menu_categories in get_menu_category_by_category_id(category['id']):
            menu_ids.append(menu_categories['menu_id'])
            stored_menu_ids.append(menu_categories['menu_id'])

        items = menus_by_ids(menu_ids)
        if len(items) > 0:
            result.append(
                MenuList(
                    category_name = category['name'],
                    items = items
                ).model_dump()
        )

    result.append(
        MenuList(
            category_name = "Other",
            items = menus_by_not_in_ids(stored_menu_ids)
        ).model_dump()
    )

    return response(result, "SUCCESS", False)