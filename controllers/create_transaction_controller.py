from services.midtrans import create_snap
from utils.response import response

def create_transaction_controller(json: dict):
    return response(create_snap())