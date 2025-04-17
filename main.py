import requests
import time
from config import SYMBOLS
from telegram_bot import send_telegram_message, send_telegram_photo
from chart_patterns import draw_candlestick_chart

def fetch_ohlcv(symbol, interval='1h', limit=100):
    url = f"https://api.lbkex.com/v2/Kline"
    params = {
        "symbol": symbol.lower(),
        "interval": interval,
        "limit": limit
    }
    try:
        response = requests.get(url, params=params)
        data = response.json()
        if "data" in data:
            df = []
            for item in data["data"]:
                df.append({
                    "timestamp": item[0],
                    "open": float(item[1]),
                    "high": float(item[2]),
                    "low": float(item[3]),
                    "close": float(item[4]),
                    "volume": float(item[5])
                })
            return df
        else:
            return None
    except Exception as e:
        print(f"خطا در دریافت دیتا برای {symbol}: {e}")
        return None

def run_bot():
    for symbol in SYMBOLS:
        for tf in ['1h', '4h']:
            ohlcv = fetch_ohlcv(symbol, tf)
            if ohlcv:
                df = ohlcv[-100:]  # فقط 100 کندل آخر
                chart_path = draw_candlestick_chart(df, symbol, tf)
                message = f"چارت {symbol.upper()} تایم‌فریم {tf}"
                send_telegram_photo(chart_path, message)
                time.sleep(3)
            else:
                send_telegram_message(f"خطا در دریافت دیتا برای {symbol.upper()} در تایم‌فریم {tf}")
                time.sleep(1)

if __name__ == "__main__":
    run_bot()
