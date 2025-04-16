import time
from lbank_api import get_ohlcv
from indicators import add_indicators
from telegram_bot import send_telegram_message
from config import SYMBOLS, INTERVAL

def analyze(symbol, interval):
    try:
        df = get_ohlcv(symbol=symbol, interval=interval, limit=100)
        df = add_indicators(df)

        latest_close = df['close'].iloc[-1]
        rsi = df['RSI'].iloc[-1]
        macd = df['MACD'].iloc[-1]
        signal = df['MACD_signal'].iloc[-1]
        atr = df['ATR'].iloc[-1]

        message = (
            f"تحلیل {symbol.upper()} در تایم‌فریم {interval}:\n"
            f"قیمت پایانی: {latest_close}\n"
            f"RSI: {rsi:.2f}\n"
            f"MACD: {macd:.2f}\n"
            f"Signal Line: {signal:.2f}\n"
            f"ATR: {atr:.2f}"
        )

        send_telegram_message(message)

    except Exception as e:
        print(f"خطا در تحلیل {symbol}: {e}")

if __name__ == "__main__":
    while True:
        for sym in SYMBOLS:
            analyze(sym, INTERVAL)
        time.sleep(900)  # اجرای هر ۱۵ دقیقه یک‌بار
