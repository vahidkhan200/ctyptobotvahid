from lbank_api import get_ohlcv
from config import SYMBOLS, INTERVAL
from telegram_bot import send_telegram_message

def main():
    for symbol in SYMBOLS:
        try:
            data = get_ohlcv(symbol, INTERVAL)
            if data:
                send_telegram_message(f"دیتای {symbol} با موفقیت دریافت شد.")
            else:
                send_telegram_message(f"دیتایی برای {symbol} پیدا نشد.")
        except Exception as e:
            send_telegram_message(f"خطا در دریافت دیتا برای {symbol}: {str(e)}")

if __name__ == "__main__":
    main()
