# main.py

from lbank import get_ohlcv
from indicators import add_indicators
from signal import generate_signal
from telegram import send_telegram_message
import time

SYMBOL = 'btc_usdt'
INTERVAL = '15min'
LIMIT = 100

def main():
    print("Starting analysis...")

    try:
        df = get_ohlcv(symbol=SYMBOL, interval=INTERVAL, limit=LIMIT)
        df = add_indicators(df)
        signals = generate_signal(df)

        if signals:
            message = f"Signal for {SYMBOL.upper()} ({INTERVAL}):\n" + "\n".join(signals)
            send_telegram_message(message)
            print("Signal sent.")
        else:
            print("No strong signal found.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    while True:
        main()
        time.sleep(900)  # هر 15 دقیقه یکبار
