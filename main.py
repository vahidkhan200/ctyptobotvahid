import requests
import time
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, SYMBOLS
from telegram_bot import send_telegram_message
from pattern_detector import is_flag_pattern

def fetch_ohlcv(symbol, interval='1h', limit=100):
    url = f"https://api.lbank.info/v2/kline.do?symbol={symbol}&type={interval}&size={limit}"
    try:
        response = requests.get(url)
        data = response.json()
        if data['result'] and 'data' in data:
            return data['data']
    except Exception as e:
        print(f"خطا در دریافت داده برای {symbol}: {e}")
    return []

timeframes = ['1h', '4h']

for symbol in SYMBOLS:
    for tf in timeframes:
        candles = fetch_ohlcv(symbol, tf)
        if not candles or len(candles) < 20:
            continue
        
        detected, pattern_name = is_flag_pattern(candles)
        if detected:
            message = f"الگوی {pattern_name} در {symbol.upper()} در تایم {tf} شناسایی شد."
            send_telegram_message(message)
        
        time.sleep(1)
