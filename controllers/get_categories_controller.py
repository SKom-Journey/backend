from utils.response import response
from services.categories import get_categories

def get_categories_controller():
    return response(get_categories())