from utils.response import response
from services.categories import create_category, get_category_by_name

def create_category_controller(category_id: str):
    checkCategoryExist = get_category_by_name(category_id)
    if checkCategoryExist == None:
        return response(create_category(category_id))
    return response("Category Name Already Exist", "ERROR", True)