import requests
import pandas as pd
import ta
from telegram_bot import send_telegram_message

def fetch_lbank_ohlcv(symbol="btc_usdt", size=100):
    url = f"https://api.lbank.info/v1/kline?symbol={symbol}&size={size}&type=day"
    try:
        response = requests.get(url)
        data = response.json()
        return data['data'] if 'data' in data else None
    except Exception as e:
        print(f"Error fetching OHLCV data: {e}")
        return None

def analyze_rsi(ohlcv):
    df = pd.DataFrame(ohlcv, columns=["timestamp", "open", "high", "low", "close", "volume"])
    df["close"] = df["close"].astype(float)
    df["rsi"] = ta.momentum.RSIIndicator(close=df["close"]).rsi()

    latest_rsi = df["rsi"].iloc[-1]

    if latest_rsi < 30:
        return "RSI: بازار اشباع فروش است. احتمال بازگشت قیمت وجود دارد."
    elif latest_rsi > 70:
        return "RSI: بازار اشباع خرید است. ممکن است قیمت اصلاح شود."
    else:
        return f"RSI فعلی: {round(latest_rsi, 2)} - وضعیت نرمال"

def main():
    ohlcv_data = fetch_lbank_ohlcv()
    if not ohlcv_data:
        send_telegram_message("دریافت دیتا از LBank با خطا مواجه شد.")
        return

    message = analyze_rsi(ohlcv_data)
    send_telegram_message(message)

if __name__ == "__main__":
    main()
