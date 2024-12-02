from utils.response import response
from services.menus import create_menu

def create_menu_controller(json: dict):
    return response(create_menu(json['title'], json['description'], json['img'], json['price']))