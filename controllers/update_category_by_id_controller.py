from utils.response import response
from services.categories import update_category_by_id

def update_category_by_id_controller(id: str, json: dict):
    return response(update_category_by_id(id, json['name']))