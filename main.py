import time
from config import SYMBOLS
from telegram_bot import send_telegram_message
from technical import fetch_ohlcv, analyze_market

def main():
    while True:
        for symbol in SYMBOLS:
            try:
                ohlcv = fetch_ohlcv(symbol)
                if ohlcv:
                    signal = analyze_market(ohlcv)
                    if signal:
                        send_telegram_message(f"سیگنال برای {symbol.upper()}:\n{signal}")
            except Exception as e:
                send_telegram_message(f"خطا در پردازش {symbol}: {str(e)}")

        # هر ۱۵ دقیقه اجرا میشه
        time.sleep(900)

if __name__ == "__main__":
    main()
