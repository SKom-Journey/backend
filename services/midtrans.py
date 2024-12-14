from configs.config import MT_CLIENT_ID, MT_SERVER_ID
import requests
from midtransclient import Snap

endpoint = "https://app.sandbox.midtrans.com/snap/v1/transactions"
snap = Snap(
    is_production=False,
    server_key=MT_SERVER_ID,
)

def create_snap():
    json = {
    "transaction_details": {
            "order_id": "ORDER-101",
            "gross_amount": 10000
        },
        "item_details": [
            {
                "id": "ITEM1",
                "price": 10000,
                "quantity": 1,
                "name": "Midtrans Bear",
                "brand": "Midtrans",
                "category": "Toys",
                "merchant_name": "Midtrans",
                "url": "http://toko/toko1?item=abc"
            }
        ],
        "customer_details": {
            "first_name": "TEST",
            "last_name": "MIDTRANSER",
            "email": "test@midtrans.com",
            "phone": "+628123456",
            "billing_address": {
                "first_name": "TEST",
                "last_name": "MIDTRANSER",
                "email": "test@midtrans.com",
                "phone": "081 2233 44-55",
                "address": "Sudirman",
                "city": "Jakarta",
                "postal_code": "12190",
                "country_code": "IDN"
            },
            "shipping_address": {
                "first_name": "TEST",
                "last_name": "MIDTRANSER",
                "email": "test@midtrans.com",
                "phone": "0 8128-75 7-9338",
                "address": "Sudirman",
                "city": "Jakarta",
                "postal_code": "12190",
                "country_code": "IDN"
            }
        },
        "enabled_payments": [
            "credit_card", "cimb_clicks",
            "bca_klikbca", "bca_klikpay", "bri_epay", "echannel", "permata_va",
            "bca_va", "bni_va", "bri_va","cimb_va", "gopay", "indomaret",
            "danamon_online", "akulaku", "shopeepay", "kredivo"
        ],
        "credit_card": {
            "secure": True,
            "channel": "migs",
            "bank": "bca",
            "installment": {
            "required": False,
            "terms": {
                "bni": [3, 6, 12],
                "mandiri": [3, 6, 12],
                "cimb": [3],
                "bca": [3, 6, 12],
                "offline": [6, 12]
            }
            },
            "whitelist_bins": [
                "48111111",
                "41111111"
            ],
                "dynamic_descriptor": {
                "merchant_name" : "Fuji Apple Inc",
                "city_name": "Jakarta",
                "country_code": "ID"
            }
        },
        "bca_va": {
            "va_number": "12345678911",
            "sub_company_code": "00000",
            "free_text": {
                "inquiry": [
                    {
                        "en": "text in English",
                        "id": "text in Bahasa Indonesia"
                    }
                ],
                "payment": [
                    {
                        "en": "text in English",
                        "id": "text in Bahasa Indonesia"
                    }
                ]
            }
        },
        "bni_va": {
            "va_number": "12345678"
        },
        "bri_va": {
            "va_number": "1234567891234"
        },
        "cimb_va": {
            "va_number": "1234567891234567"
        },  
        "permata_va": {
            "va_number": "1234567890",
            "recipient_name": "SUDARSONO"
        },
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
            "duration": 1,
            "unit": "hours"
        }
    }
    
    return snap.create_transaction(json)