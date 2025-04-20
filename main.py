# main.py

from exchange.lbank import get_candles
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID
import requests
import time

# ارسال پیام به تلگرام
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }
    response = requests.post(url, data=data)
    if response.status_code != 200:
        print("تلگرام خطا:", response.text)

# بررسی یک الگوی ساده: روند صعودی کندل‌ها
def detect_uptrend(candles):
    closing_prices = [float(c[4]) for c in candles]  # price_close
    return all(closing_prices[i] < closing_prices[i+1] for i in range(len(closing_prices)-1))

# اجرای اصلی ربات
def main():
    print("شروع ربات تریدر...")
    while True:
        candles = get_candles(symbol='btc_usdt', interval='5min', size=5)
        if not candles:
            print("خطا در دریافت کندل")
            time.sleep(60)
            continue

        if detect_uptrend(candles):
            last_price = candles[-1][4]
            message = (
                f"سیگنال لانگ شناسایی شد!\n\n"
                f"رمز ارز: BTC/USDT\n"
                f"پوزیشن: لانگ\n"
                f"نقطه ورود: {last_price}\n"
                f"تارگت ۱: {round(float(last_price) * 1.01, 2)}\n"
                f"تارگت ۲: {round(float(last_price) * 1.02, 2)}\n"
                f"حد ضرر: {round(float(last_price) * 0.99, 2)}\n"
                f"لورج پیشنهادی: 5x\n"
                f"بر اساس الگو: روند صعودی ساده"
            )
            send_telegram_message(message)
        else:
            print("الگویی شناسایی نشد.")

        time.sleep(300)  # هر ۵ دقیقه چک کن

if __name__ == "__main__":
    main()
