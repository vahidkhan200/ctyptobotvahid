import os import time from lbank_api import get_symbols, get_klines from telegram_bot import send_telegram_signal from strategies import analyze_symbol  # فایل strategies.py باید موجود باشه

تنظیمات کلی

TIMEFRAME = '1h' SYMBOLS = ['BTC_USDT', 'ETH_USDT', 'BNB_USDT'] INTERVAL = 60 * 60  # هر یک ساعت یک بار اجرا میشه

def main(): print("شروع آنالیز...") for symbol in SYMBOLS: print(f"در حال بررسی: {symbol}") df = get_klines(symbol, TIMEFRAME) if df is None or df.empty: print(f"داده‌ای برای {symbol} پیدا نشد.") continue

signal = analyze_symbol(symbol, df)
    if signal:
        print(f"سیگنال پیدا شد برای {symbol}")
        formatted = f"""

نام ارز: {signal['symbol']} تایم فریم: {TIMEFRAME} نقطه ورود: {signal['entry']} تارگت ۱: {signal['target1']} تارگت ۲: {signal['target2']} حد ضرر: {signal['stoploss']} لورج: {signal['leverage']} """ send_telegram_signal(formatted) else: print(f"سیگنالی برای {symbol} پیدا نشد.")

if name == "main": while True: main() print("در انتظار اجرای بعدی...") time.sleep(INTERVAL)
