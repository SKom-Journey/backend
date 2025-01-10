from utils.response import response
from services.menus import update_menu_by_id
from utils.save_file import save_file

def update_menu_by_id_controller(id: str, form: dict, file):
    img_url = save_file(file)

    data = {
        "img": img_url,
        "title": form.get('title'),
        "description": form.get('description'),
        "price": int(form.get('price')),
    }
    return response(update_menu_by_id(id, data))