from configs.config import CLIENT_WEB_URL

def menu_detail_url(menu_id: str):
    return CLIENT_WEB_URL + '/detail/' + menu_id