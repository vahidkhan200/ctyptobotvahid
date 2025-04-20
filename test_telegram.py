# test_telegram.py

import requests
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

def send_test_message():
    url = f"https://api.telegram.org/bot{7769467888:AAHrxpGS8xdM8EzJHz5qVjS774arSP1VfLU}/sendMessage"
    data = {
        "chat_id": 392018191,
        "text": "سلام! این یک پیام تستی از ربات تریدره."
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print("پیام با موفقیت ارسال شد.")
    else:
        print("خطا در ارسال پیام:", response.text)

send_test_message()
