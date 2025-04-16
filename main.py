import requests
from telegram_bot import send_telegram_message

def fetch_lbank_ohlcv(symbol="btc_usdt", size=100):
    url = f"https://api.lbank.info/v1/kline?symbol={symbol}&size={size}&type=day"
    try:
        response = requests.get(url)
        data = response.json()
        return data['data'] if 'data' in data else None
    except Exception as e:
        print(f"Error fetching OHLCV data for {symbol}: {e}")
        return None

def main():
    ohlcv_data = fetch_lbank_ohlcv()

    if not ohlcv_data:
        send_telegram_message("دریافت دیتا از LBank با خطا مواجه شد.")
        return

    # تحلیل ساده: چک کنیم قیمت امروز بیشتر از دیروزه؟
    latest = ohlcv_data[-1]
    previous = ohlcv_data[-2]

    latest_close = float(latest[4])
    previous_close = float(previous[4])

    if latest_close > previous_close:
        send_telegram_message("قیمت بیت‌کوین صعودی است.")
    else:
        send_telegram_message("قیمت بیت‌کوین نزولی یا بدون تغییر است.")

if __name__ == "__main__":
    main()
