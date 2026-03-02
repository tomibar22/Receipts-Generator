import requests
import json
from config.settings import NOTION_TOKEN, DATABASE_ID

def create_receipts(morning_token, start_date, end_date):
    
    # NOTION - DATABASE QUERY  
    headers = {
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28",
    }
  
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
  
    payload = {
        "filter": {
            "and": [
                {
                    "property": "דו״ח",
                    "checkbox": {
                        "equals": True
                    }
                },
                {
                    "property": "תאריך קבלה",
                    "date": {
                        "on_or_after": start_date
                    }
                },
                {
                    "property": "תאריך קבלה",
                    "date": {
                        "on_or_before": end_date
                    }
                },
                {
                    "property": "קבלה",
                    "checkbox": {
                        "equals": False
                    }
                },
                {
                    "property": "חשבונית",
                    "checkbox": {
                        "equals": False
                    }
                },
            ]
        }
    }
  
    response = requests.post(url, headers=headers, json=payload)
    data = response.json()
    pages = data["results"]
    
    for page in reversed(pages): 
        
        # NOTION - SETTING RELEVANT VARIABLES
        date = page["properties"]["תאריך קבלה"]["date"]["start"]
        income = page["properties"]["הכנסה"]["title"][0]["text"]["content"]
        amount = page["properties"]["סכום"]["number"]
        payer = page["properties"]["שולם ע״י"]["select"]["name"]

        if page["properties"]["אמצעי"]["select"]["name"] == "מזומן":
         medium = 1
        elif page["properties"]["אמצעי"]["select"]["name"] == "העברה":
         medium = 4
        elif page["properties"]["אמצעי"]["select"]["name"] == "צ׳ק":
         medium = 2
        elif page["properties"]["אמצעי"]["select"]["name"] == "אפליקציית תשלום":
         medium = 10

        if page["properties"]["אפליקצייה"]["select"] == None:
         app = ""
        elif page["properties"]["אפליקצייה"]["select"]["name"] == "ביט":
         app = 1
        elif page["properties"]["אפליקצייה"]["select"]["name"] == "פיי-בוקס":
         app = 3
        else:
          app = ""


        # MORNING - CREATING DOCUMENT
        url = "https://api.greeninvoice.co.il/api/v1/documents"

        payload = json.dumps({
        "description": income,
        "type": 400,
        "vatType": 0,
        "lang": "he",
        "currency": "ILS",
        "client": {
            "name": payer,
            "add": True,
            "self": False,
        },
        "rounding": False,
        "income": [
            {
            "description": income,
            "quantity": 1,
            "price": amount,
            "currency": "ILS",
            "vatType": 0
            },
        ],
        "payment": [
            {
            "type": medium,
            "price": amount,
            "currency": "ILS",
            "date": date,
            "appType":app
            },
        ]
        })
        headers = {
        'Authorization': morning_token,
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(f'{date} - {income} - {payer} - {amount}')


def Receipt_Checkbox(start_date, end_date):
    
    # NOTION - DATABASE QUERY
    headers = {
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28",
    }
  
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
  
    payload = {
        "filter": {
            "and": [
                {
                    "property": "דו״ח",
                    "checkbox": {
                        "equals": True
                    }
                },
                {
                    "property": "תאריך קבלה",
                    "date": {
                        "on_or_after": start_date
                    }
                },
                {
                    "property": "תאריך קבלה",
                    "date": {
                        "on_or_before": end_date
                    }
                },
                {
                    "property": "קבלה",
                    "checkbox": {
                        "equals": False
                    }
                },
                {
                    "property": "חשבונית",
                    "checkbox": {
                        "equals": False
                    }
                }
            ]
        }
    }
  
    response = requests.post(url, headers=headers, json=payload)
    data = response.json()
    pages = data["results"]
    
    for page in reversed(pages): 
        
        # NOTION - SETTING RELEVANT VARIABLES
        page_id = page["id"]

        
        # NOTION - RECEIPT CHECKBOX UPDATE
        url2 = f"https://api.notion.com/v1/pages/{page_id}"

        payload2 = {
        "properties": {
            "קבלה": {
                "checkbox": True,
                },
            },
        }

        requests.patch(url2, headers=headers, json=payload2)
