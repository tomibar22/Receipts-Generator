import os
from dotenv import load_dotenv

load_dotenv()

NOTION_TOKEN = os.getenv("NOTION_SECRET")
DATABASE_ID = os.getenv("DATABASE_ID")
MORNING_SECRET = os.getenv("MORNING_SECRET")
MORNING_ID = os.getenv("MORNING_ID")
