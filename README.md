# Receipts Generator

Automated receipt generator for piano teaching business. Pulls income entries from Notion and creates receipts via Green Invoice (חשבונית ירוקה) API.

## Setup

1. Copy `.env.example` to `.env` and fill in your credentials
2. Install dependencies: `pip install -r requirements.txt`
3. Run: `python main.py`

## What it does

1. Queries Notion database for income entries from the previous month that haven't received a receipt yet
2. Creates a receipt (type 400) in Green Invoice for each entry
3. Marks the receipt checkbox in Notion as completed

## Environment Variables

| Variable | Description |
|---|---|
| `NOTION_SECRET` | Notion integration token |
| `DATABASE_ID` | Notion database ID for income tracking |
| `MORNING_SECRET` | Green Invoice API secret |
| `MORNING_ID` | Green Invoice API ID |
