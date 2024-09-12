import requests
import base64
from datetime import datetime
from app.config import settings

def generate_token():
    api_key = base64.b64encode(f"{settings.CONSUMER_KEY}:{settings.CONSUMER_SECRET}".encode("utf-8")).decode("utf-8")
    url = f"{settings.MPESA_BASE_URL}/oauth/v1/generate?grant_type=client_credentials"
    response = requests.get(url, headers={"Authorization": "Basic " + api_key})
    response.raise_for_status()
    return response.json()["access_token"]

def send_stk_push(phone_number: str, amount:int):
    print('get token')
    access_token = generate_token()
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    password = base64.b64encode(f"{settings.SHORTCODE}{settings.PASSKEY}{timestamp}".encode("utf-8")).decode("utf-8")

    stk_push_data = {
        "BusinessShortCode" : settings.SHORTCODE,
        "Password":password,
        "Timestamp":timestamp,
        "TransactionType":"CustomerPayBillOnline",
        "Amount":amount,
        "PartyA":phone_number,
        "PartyB":settings.SHORTCODE,
        "PhoneNumber":phone_number,
        "CallBackURL":settings.CALLBACK_URL,
        "AccountReference":"TestPayment",
        "TransactionDesc":"Payment for service"
    }
    print(stk_push_data)
    stk_push_url = f"{settings.MPESA_BASE_URL}/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization":f"Bearer " + access_token, 
               "Content-Type":"application/json"}

    response = requests.post(stk_push_url, json=stk_push_data, headers=headers)
    response.raise_for_status()

    return response.json()