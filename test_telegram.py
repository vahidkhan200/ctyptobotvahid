import requests

# توکن ربات رو اینجا بذار
BOT_TOKEN = '7769467888:AAHrxpGS8xdM8EzJHz5qVjS774arSP1VfLU'

# چت آیدی عددی (مثلاً 123456789) یا username با @
CHAT_ID = '392018191'

# پیام تستی
message = "سلام! این یه پیام تستی از ربات تریدر هست."

# ارسال پیام به تلگرام
url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
data = {
    "chat_id": CHAT_ID,
    "text": message
}

response = requests.post(url, data=data)

# نمایش خروجی برای بررسی
print("Status Code:", response.status_code)
print("Response:", response.text)
