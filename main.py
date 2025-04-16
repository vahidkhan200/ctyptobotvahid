import requests
from config import SYMBOLS
from telegram_bot import send_telegram_message

def fetch_ohlcv(symbol):
    url = f"https://api.lbkex.com/v2/kline.do?symbol={symbol}&size=50&type=1hour"
    try:
        response = requests.get(url)
        data = response.json()
        if "datas" in data:
            return data["datas"]
        return None
    except Exception as e:
        print(f"Error fetching OHLCV data for {symbol}: {e}")
        send_telegram_message(f"دریافت دیتا از LBank برای {symbol} با خطا مواجه شد.")
        return None

def analyze_data(ohlcv_data):
    if not ohlcv_data or len(ohlcv_data) < 2:
        return None
    latest_close = float(ohlcv_data[-1][2])
    previous_close = float(ohlcv_data[-2][2])
    if latest_close > previous_close:
        return "سیگنال خرید"
    elif latest_close < previous_close:
        return "سیگنال فروش"
    else:
        return None

for symbol in SYMBOLS:
    ohlcv = fetch_ohlcv(symbol)
    signal = analyze_data(ohlcv)
    if signal:
        msg = f"{signal} برای {symbol.upper()}"
        print(msg)
        send_telegram_message(msg)
