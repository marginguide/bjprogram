import requests, sqlite3
import pandas as pd
from config import MALL_ID
from auth import get_access
import json
 # 본인의 쇼핑몰 ID
access_token = get_access()
url = f"""https://{MALL_ID}.cafe24api.com/api/v2/admin/orders?
            start_date=2025-02-20&end_date=2025-02-27&
            payment_status=P"""
headers = {
    'Authorization': f"Bearer {access_token}",
    'Content-Type': "application/json",
    'X-Cafe24-Api-Version': f"2024-12-01"
    }
response = requests.request("GET", url, headers=headers)
print(type(response.text))
result = json.loads(response.text)

orders = result['orders']
for order in orders:
    buyer_name = order['buyer_name']
    receiver_name = order['receiver_name']
    payment_status = order['payment_status']
    buyer_name = order['buyer_name']
    buyer_name = order['buyer_name']
    buyer_name = order['buyer_name']
    buyer_name = order['buyer_name']
    buyer_name = order['buyer_name']
    buyer_name = order['buyer_name']
    buyer_name = order['buyer_name']
    buyer_name = order['buyer_name']