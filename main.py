import time
from config import SYMBOLS
from technical import fetch_ohlcv, analyze_market
from telegram_bot import send_telegram_message

while True:
    for symbol in SYMBOLS:
        print(f"بررسی {symbol}...")
        df = fetch_ohlcv(symbol)
        signal = analyze_market(df)

        if signal:
            message = f"سیگنال برای {symbol.upper()}:\n{signal}"
            send_telegram_message(message)

    print("پایان بررسی - 15 دقیقه استراحت...")
    time.sleep(900)  # اجرای هر ۱۵ دقیقه یکبار
