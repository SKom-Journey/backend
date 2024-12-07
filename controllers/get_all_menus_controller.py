from utils.response import response
from services.menus import menus

def get_all_menus_controller():
    return response(menus(''))