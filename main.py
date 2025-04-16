from lbank_api import get_ohlcv
from telegram_bot import send_telegram_message

df = get_ohlcv('btc_usdt', interval='15min', limit=50)

if not df.empty:
    last_close = df['close'].iloc[-1]
    msg = f"آخرین قیمت BTC/USDT در تایم‌فریم ۱۵ دقیقه: {last_close}"
    send_telegram_message(msg)
else:
    send_telegram_message("دریافت دیتا از LBank با خطا مواجه شد.")
