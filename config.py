# config.py
import os

TELEGRAM_BOT_TOKEN = os.getenv("7808088088:AAGu9D1Vr5Iq6lrrE7P2jbMr32_-K6Y8wF4")
TELEGRAM_CHAT_ID = os.getenv("392018191")

SYMBOLS = [
    "btc_usdt", "eth_usdt", "bnb_usdt", "sol_usdt", "ada_usdt", "xrp_usdt",
    "dot_usdt", "matic_usdt", "ltc_usdt", "grt_usdt", "grs_usdt",
    "not_usdt", "doge_usdt", "xlm_usdt", "hbar_usdt", "xdc_usdt"
]

# تایم‌فریم تحلیل
INTERVAL = '15min'

# آدرس API صرافی LBank
LBANK_API_URL = 'https://api.lbkex.com'

# تنظیمات تحلیل تکنیکال
MACD_FAST = 12
MACD_SLOW = 26
MACD_SIGNAL = 9

RSI_PERIOD = 14
EMA_PERIOD = 20
ATR_PERIOD = 14
