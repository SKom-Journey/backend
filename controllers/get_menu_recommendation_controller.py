from utils.response import response
from utils.ner_module import get_entities
from services.menus import find_by_entities
from services.chats import create_chat, chats_by_user_id
from utils.construct_query import construct_query

def get_menu_recommendation_controller(text: str, user_id: str):
    entities = get_entities(text.replace("?", ""))
    query = {}

    for key, values in entities.items():
        if values:
            construct_query(key, values, query)
    
    menu_ids = []
    menus = find_by_entities(query)
    for menu in menus:
        menu_ids.append(menu['id'])

    create_chat(user_id, text, menu_ids)

    return response(chats_by_user_id(user_id, 1, -1))