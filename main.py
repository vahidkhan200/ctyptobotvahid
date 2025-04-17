import ccxt
import time
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, SYMBOLS
from telegram_bot import send_telegram_message
from strategies import analyze_symbol

exchange = ccxt.lbank({
    'enableRateLimit': True,
})

def fetch_ohlcv(symbol, timeframe='1h', limit=100):
    try:
        ohlcv = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
        return ohlcv
    except Exception as e:
        print(f"خطا در دریافت داده {symbol}: {e}")
        return None

def main():
    for symbol in SYMBOLS:
        print(f"در حال بررسی {symbol}")
        ohlcv = fetch_ohlcv(symbol)
        if ohlcv:
            messages = analyze_symbol(symbol, ohlcv)
            for msg in messages:
                send_telegram_message(msg)
        time.sleep(1.5)  # جلوگیری از محدودیت API

if __name__ == '__main__':
    while True:
        main()
        print("پایان بررسی، شروع دور جدید بعد از 60 دقیقه...")
        time.sleep(3600)  # اجرای هر ساعت
