from flask import Flask, request
from controllers.get_menu_recommendation_controller import get_menu_recommendation_controller
from controllers.get_menus_controller import get_menus_controller
from dotenv import load_dotenv
from flask_socketio import SocketIO, emit
from flask_cors import CORS
from controllers.get_user_chats_controller import get_user_chats_controller
from controllers.get_qr_controller import get_qr_controller
from controllers.get_qrs_controller import get_qrs_controller
from controllers.create_qr_controller import create_qr_controller
from controllers.delete_qr_controller import delete_qr_controller
from controllers.create_order_controller import create_order_controller
from controllers.get_orders_controller import get_orders_controller
from controllers.register_user_controller import register_user_controller
from controllers.login_user_controller import login_user_controller
from controllers.create_category_controller import create_category_controller
from controllers.delete_category_controller import delete_category_controller
from controllers.create_menu_category_controller import create_menu_category_controller
from controllers.delete_menu_category_controller import delete_menu_category_controller
from controllers.create_cart_controller import create_cart_controller
from controllers.delete_cart_controller import delete_cart_controller
from controllers.get_user_carts_controller import get_user_carts_controller
from controllers.update_cart_note_by_id_controller import update_cart_note_by_id_controller
from controllers.login_admin_controller import login_admin_controller
from controllers.finish_order_controller import finish_order_controller
from controllers.delete_user_chats_controller import delete_user_chats_controller
from controllers.delete_menu_controller import delete_menu_controller
from controllers.create_menu_controller import create_menu_controller
from controllers.get_all_menus_controller import get_all_menus_controller
from controllers.update_menu_by_id_controller import update_menu_by_id_controller
from controllers.register_oauth_user_controller import register_oauth_user_controller
from controllers.delete_user_controller import delete_user_controller
from controllers.get_menu_controller import get_menu_controller
from controllers.get_profile_controller import get_profile_controller
from controllers.update_user_name_controller import update_user_name_controller
from controllers.refresh_session_controller import refresh_session_controller
from controllers.create_transaction_controller import create_transaction_controller
from configs.config import CORS_ALLOWED_ORIGINS, DEBUG_MODE
from middleware.check_user_jwt import check_user_jwt
from middleware.get_refresh_token import get_refresh_token

load_dotenv()

app = Flask(__name__)
CORS(app, origins=CORS_ALLOWED_ORIGINS, supports_credentials=True)
socketio = SocketIO(app, cors_allowed_origins=CORS_ALLOWED_ORIGINS)

@app.post('/transaction')
def create_transaction():
    return create_transaction_controller(request.get_json())

@app.get('/me')
@check_user_jwt
def get_profile(payload: dict):
    return get_profile_controller(payload)

@app.post('/oauths/google/<access_token>')
def register_user_with_google(access_token: str):
    return register_oauth_user_controller(access_token)

@app.put('/carts/<cart_id>')
def update_cart_note_by_id(cart_id: str):
    return update_cart_note_by_id_controller(cart_id, request.get_json())

@app.get('/carts/<user_id>')
def get_cart(user_id: str):
    return get_user_carts_controller(user_id)

@app.delete('/carts')
def delete_cart():
    return delete_cart_controller(request.get_json())

@app.post('/carts')
def create_cart():
    return create_cart_controller(request.get_json())

@app.put('/users/<user_id>')
def update_user_name(user_id: str):
    return update_user_name_controller(user_id, request.get_json())

@app.delete('/users/<user_id>')
def delete_user(user_id: str):
    return delete_user_controller(user_id)

@app.post('/auths/users/login')
def login_user():
    return login_user_controller(request.get_json())

@app.post('/auths/users/register')
def register_user():
    return register_user_controller(request.get_json())

@app.post('/auths/admins/login')
def login_admin():
    return login_admin_controller(request.get_json())

@app.post('/auths/refresh')
@get_refresh_token
def refresh_token(refresh_token: str):
    return refresh_session_controller(refresh_token)

@app.put('/orders/<order_id>')
def finish_order(order_id: str):
    return finish_order_controller(order_id)

@app.get('/orders')
def get_orders():
    return get_orders_controller()

@app.post('/orders')
def create_order():
    return create_order_controller(request.get_json())

@app.delete('/chats/<user_id>')
def delete_chats_by_user_id(user_id: str):
    return delete_user_chats_controller(user_id)

@app.get('/chats/<user_id>')
def get_user_chats(user_id: str):
    return get_user_chats_controller(user_id)

@app.get('/qrs/<table_number>')
def get_qr(table_number: str):
    return get_qr_controller(table_number)

@app.get('/qrs')
def get_qrs():
    return get_qrs_controller()

@app.post('/qrs')
def create_qr():
    return create_qr_controller(request.get_json())

@app.delete('/qrs/<qr_id>')
def delete_qr(qr_id: str):
    return delete_qr_controller(qr_id)

@app.delete('/menus//<menu_id>')
def delete_menu(menu_id: str):
    return delete_menu_controller(menu_id)

@app.post('/menus')
def create_menu():
    return create_menu_controller(request.get_json())

@app.get('/menus/all')
def get_all_menus():
    return get_all_menus_controller()

@app.get('/menus/<menu_id>')
def get_menu(menu_id: str):
    return get_menu_controller(menu_id)

@app.put('/menus/<menu_id>')
def update_menu(menu_id: str):
    return update_menu_by_id_controller(menu_id, request.get_json())

@app.get('/menus')
def get_menus():
    return get_menus_controller(request.args.get('keyword', type=str))

@app.post('/categories')
def create_category():
    return create_category_controller(request.get_json())

@app.delete('/categories/<category_id>')
def delete_category(category_id: str):
    return delete_category_controller(category_id)

@app.post('/menu-categories')
def create_menu_category():
    return create_menu_category_controller(request.get_json())

@app.delete('/menu-categories')
def delete_menu_category():
    return delete_menu_category_controller(request.get_json())

@socketio.on('menu_recommendation')
def menu_recommendation(text, user_id):
    recommendation = get_menu_recommendation_controller(text, user_id)
    emit('menu_recommendation_response', recommendation)

if __name__ == '__main__':
    socketio.run(app, debug=DEBUG_MODE, port=8000, host='0.0.0.0')