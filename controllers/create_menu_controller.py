from utils.response import response
from services.menus import create_menu
from utils.save_file import save_file

def create_menu_controller(form: dict, file):
    img_url = save_file(file)
    return response(create_menu(form.get('title'), form.get('description'), img_url, form.get('price')))