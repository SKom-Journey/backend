from configs.config import MT_SERVER_ID
from midtransclient import Snap
from services.carts import get_carts_by_user_id
from services.users import user_by_id
from uuid import uuid4
from utils.menu_detail_url import menu_detail_url

snap = Snap(
    is_production=False,
    server_key=MT_SERVER_ID,
)

def create_transaction(user_id: str):
    items = []
    gross_amount = 0
    carts = get_carts_by_user_id(user_id)
    user = user_by_id(user_id)

    for cart in carts:
        price = cart['menu']['price'] * cart['quantity']
        items.append({
            "id": cart['menu']['id'],
            "price": cart['menu']['price'],
            "quantity": cart['quantity'],
            "name": cart['menu']['title'],
            "merchant_name": "Ryomu Restaurant",
            "brand": "Ryomu Restaurant",
            "url": menu_detail_url(cart['menu']['id']),
            "category": "Food & Beverage"
        })
        gross_amount += price

    json = {
        "transaction_details": {
            "order_id": str(uuid4()),
            "gross_amount": gross_amount
        },
        "item_details": items,
        "customer_details": {
            "first_name": user['name'],
            "last_name": "",
            "email": user['email']
        },
        "enabled_payments": [
            "gopay", "shopeepay"
        ],
        "shopeepay": {
            "callback_url": "http://shopeepay.com"
        },
        "gopay": {
            "enable_callback": True,
            "callback_url": "http://gopay.com"
        },
        "callbacks": {
            "finish": "https://demo.midtrans.com"
        },
        "page_expiry": {
            "duration": 5,
            "unit": "minutes"
        }
    }
    
    return snap.create_transaction(json)
    # return json