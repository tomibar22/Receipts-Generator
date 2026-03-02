from datetime import date, timedelta
from app.notion_api import create_receipts, Receipt_Checkbox
from app.greeninvoice_api import get_morning_token

def main():
    
    today = date.today()
    first_day_of_month = date(today.year, today.month, 1)
    last_day_of_december = date(today.year + 1, 1, 1) - timedelta(days=1)
    last_day_of_prev_month = first_day_of_month - timedelta(days=1)
    first_day_of_prev_month = date(last_day_of_prev_month.year, last_day_of_prev_month.month, 1)
    first_day_of_year = date(today.year, 1, 1)

    if today.month == 12 and today.day > 22:
        start_date = first_day_of_month.strftime('%Y-%m-%d')
        end_date = last_day_of_december.strftime('%Y-%m-%d')
    else:
        start_date = first_day_of_prev_month.strftime('%Y-%m-%d')
        end_date = last_day_of_prev_month.strftime('%Y-%m-%d')

    morning_token = get_morning_token()

    create_receipts(morning_token, start_date, end_date)
    Receipt_Checkbox(start_date, end_date)

if __name__ == "__main__":
    main()
