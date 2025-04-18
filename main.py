# main.py

import time
import ccxt
import pandas as pd
from strategies import analyze_symbol
from telegram_bot import send_telegram_message
from config import SYMBOLS, TIMEFRAMES

exchange = ccxt.binance()

def fetch_ohlcv(symbol, timeframe='1h', limit=100):
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    return df

if __name__ == "__main__":
    while True:
        for symbol in SYMBOLS:
            for tf in TIMEFRAMES:
                try:
                    df = fetch_ohlcv(symbol, tf)
                    signal = analyze_symbol(symbol, tf, df)
                    if signal:
                        send_telegram_message(signal)
                except Exception as e:
                    print(f"خطا در {symbol} / {tf}: {str(e)}")
        time.sleep(300)  # اجرا هر ۵ دقیقه
