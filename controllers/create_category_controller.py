from utils.response import response
from services.categories import create_category, get_category_by_name

def create_category_controller(json: dict):
    checkCategoryExist = get_category_by_name(json['name'])
    if checkCategoryExist == None:
        return response(create_category(json['name']))
    return response("Category Name Already Exist", "ERROR", True)