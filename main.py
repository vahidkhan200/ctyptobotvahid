from lbank_api import get_ohlcv
from indicators import add_indicators
import time

def analyze(symbol: str, interval: str):
    print(f"در حال دریافت داده برای {symbol} با تایم‌فریم {interval}...")
    df = get_ohlcv(symbol=symbol, interval=interval, limit=100)

    if df is None or df.empty:
        print("داده‌ای دریافت نشد.")
        return

    df = add_indicators(df)
    print("تحلیل کامل شد. نتایج:")
    print(df.tail())

def main():
    # لیست ارزها و تایم‌فریم‌ها
    symbols = ['btc_usdt', 'eth_usdt', 'sol_usdt']
    intervals = ['15min', '1h']

    while True:
        for symbol in symbols:
            for interval in intervals:
                analyze(symbol, interval)

        # هر ۱۵ دقیقه یک بار تحلیل انجام شود
        print("در حال استراحت تا اجرای بعدی...")
        time.sleep(900)  # 900 ثانیه = 15 دقیقه

if __name__ == '__main__':
    main()
