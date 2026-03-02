import requests
import json
from config.settings import MORNING_SECRET, MORNING_ID

def get_morning_token():
    url = "https://api.greeninvoice.co.il/api/v1/account/token"
    payload = json.dumps({
    "id": MORNING_ID,
    "secret": MORNING_SECRET
    })
    headers = {
    'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    tokendata = json.loads(response.text)
    MORNING_TOKEN = "Bearer" + tokendata['token']
    return MORNING_TOKEN
