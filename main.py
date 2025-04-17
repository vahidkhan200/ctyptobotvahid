import ccxt
import time
from strategies import analyze_symbol
from telegram_bot import send_telegram_message
from config import SYMBOLS

exchange = ccxt.lbank()

def fetch_ohlcv(symbol):
    try:
        return exchange.fetch_ohlcv(symbol, timeframe='1h', limit=100)
    except Exception as e:
        send_telegram_message(f"خطا در دریافت دیتا برای {symbol}: {str(e)}")
        return None

for symbol in SYMBOLS:
    print(f"بررسی ارز: {symbol}")
    ohlcv = fetch_ohlcv(symbol)
    if ohlcv:
        signal = analyze_symbol(ohlcv)
        if signal:
            send_telegram_message(f"سیگنال برای {symbol}: {signal}")
    time.sleep(1)
