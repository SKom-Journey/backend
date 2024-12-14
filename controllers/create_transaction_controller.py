from services.midtrans import create_transaction
from utils.response import response

def create_transaction_controller(json: dict):
    return response(create_transaction(json['user_id']))