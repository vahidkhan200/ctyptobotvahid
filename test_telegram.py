# test_telegram.py

import requests
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

def send_test_message():
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": "سلام! این یک پیام تستی از ربات تریدره."
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print("پیام با موفقیت ارسال شد.")
    else:
        print("خطا در ارسال پیام:", response.text)

send_test_message()
