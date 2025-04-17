import time
from config import SYMBOLS
from strategies import analyze_symbol
from telegram_bot import send_telegram_message

previous_signals = {}

while True:
    for symbol in SYMBOLS:
        try:
            print(f"در حال بررسی: {symbol}")
            result = analyze_symbol(symbol)

            if result and previous_signals.get(symbol) != result:
                send_telegram_message(f"{symbol}: {result}")
                previous_signals[symbol] = result

            elif not result:
                previous_signals[symbol] = None

        except Exception as e:
            print(f"خطا در بررسی {symbol}: {e}")
            send_telegram_message(f"خطا در بررسی {symbol}: {e}")
    
    print("منتظر 10 دقیقه بعد...")
    time.sleep(600)
