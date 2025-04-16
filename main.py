import requests
import pandas as pd
from telegram_bot import send_telegram_message

symbols = [
    "btc_usdt", "eth_usdt", "bnb_usdt", "sol_usdt", "ada_usdt", "xrp_usdt", "dot_usdt",
    "link_usdt", "avax_usdt", "doge_usdt", "matic_usdt", "shib_usdt", "grs_usdt", "not_usdt",
    "dogz_usdt", "xlm_usdt", "hbar_usdt", "xdc_usdt"
]

def fetch_ohlcv(symbol):
    url = f"https://api.lbkex.com/v2/kline.do?symbol={symbol}&size=100&type=1min"
    try:
        response = requests.get(url)
        data = response.json()
        if "datas" not in data or "klines" not in data["datas"]:
            return None
        df = pd.DataFrame(data["datas"]["klines"])
        df.columns = ["timestamp", "open", "high", "low", "close", "volume"]
        df["close"] = df["close"].astype(float)
        return df
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")
        return None

def analyze_and_alert(symbol):
    df = fetch_ohlcv(symbol)
    if df is None or df.empty:
        print(f"No data for {symbol}")
        return

    df["rsi"] = df["close"].pct_change().rolling(14).apply(
        lambda x: 100 - (100 / (1 + x[x > 0].mean() / abs(x[x < 0].mean()))) if x[x < 0].mean() != 0 else 50
    )

    latest_rsi = df["rsi"].iloc[-1]
    message = None

    if latest_rsi < 30:
        message = f"✅ سیگنال خرید احتمالی ({symbol.upper()}) - RSI: {latest_rsi:.2f}"
    elif latest_rsi > 70:
        message = f"⚠️ سیگنال فروش احتمالی ({symbol.upper()}) - RSI: {latest_rsi:.2f}"

    if message:
        print(message)
        send_telegram_message(message)

if __name__ == "__main__":
    for symbol in symbols:
        analyze_and_alert(symbol)
