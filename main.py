import time
from config import SYMBOLS, TIMEFRAMES, CHECK_INTERVAL
from telegram_bot import send_telegram_message
from strategies.signal_builder import analyze_symbol

while True:
    for symbol in SYMBOLS:
        for timeframe in TIMEFRAMES:
            signal = analyze_symbol(symbol, timeframe)
            if signal:
                send_telegram_message(signal)
            time.sleep(1)
    time.sleep(CHECK_INTERVAL)
