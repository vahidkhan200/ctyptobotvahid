import os
import time

from lbank_api import get_symbols, get_klines
from telegram_bot import send_telegram_signal
from strategies import analyze_symbol  # مطمئن شو strategies.py وجود داره و متد analyze_symbol در اون هست

def main():
    symbols = get_symbols()
    timeframes = ["1h", "4h"]

    while True:
        for symbol in symbols:
            for tf in timeframes:
                try:
                    klines = get_klines(symbol, tf)
                    signal = analyze_symbol(symbol, tf, klines)

                    if signal:
                        send_telegram_signal(signal)
                except Exception as e:
                    print(f"Error processing {symbol} on {tf}: {str(e)}")
        time.sleep(60 * 15)  # هر ۱۵ دقیقه یک‌بار بررسی می‌کنه

if __name__ == "__main__":
    main()
