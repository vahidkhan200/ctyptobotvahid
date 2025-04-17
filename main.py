import time
import csv
from datetime import datetime
from config import SYMBOLS
from strategies import analyze_symbol
from telegram_bot import send_telegram_message

previous_signals = {}

def log_signal(symbol, signal):
    with open("signals_log.csv", "a", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), symbol, signal, "1h & 4h"])

while True:
    for symbol in SYMBOLS:
        try:
            print(f"در حال بررسی: {symbol}")
            result = analyze_symbol(symbol)

            if result and previous_signals.get(symbol) != result:
                send_telegram_message(f"{symbol}: {result}")
                log_signal(symbol, result)
                previous_signals[symbol] = result

            elif not result:
                previous_signals[symbol] = None

        except Exception as e:
            print(f"خطا در بررسی {symbol}: {e}")
            send_telegram_message(f"خطا در بررسی {symbol}: {e}")
    
    print("منتظر 10 دقیقه بعد...")
    time.sleep(600)
