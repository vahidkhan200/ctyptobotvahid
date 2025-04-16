import requests
import pandas as pd
import time
from telegram_bot import send_telegram_message
from ta_utils import is_buy_signal
from config import SYMBOLS

def fetch_ohlcv(symbol):
    try:
        url = f"https://api.lbank.info/v2/kline.do?symbol={symbol}&type=15min&size=100"
        response = requests.get(url)
        data = response.json()
        df = pd.DataFrame(data['data'], columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        df['close'] = pd.to_numeric(df['close'])
        return df
    except Exception as e:
        print(f"خطا در دریافت دیتا از LBank برای {symbol}: {e}")
        return None

for symbol in symbols:
    df = fetch_ohlcv(symbol)
    if df is not None and is_buy_signal(df):
        message = f"سیگنال خرید روی {symbol.upper()} ظاهر شد!"
        send_telegram_message(message)

time.sleep(3)  # اگر بخوایم با فاصله اجرا کنیم یا بعداً بزاریم تو حلقه
