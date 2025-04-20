import ccxt
from config import LBANK_API_KEY, LBANK_API_SECRET

# اتصال به Lbank API
def create_lbank_client():
    lbank = ccxt.lbank({
        'apiKey': LBANK_API_KEY,
        'secret': LBANK_API_SECRET,
        'enableRateLimit': True,
    })
    return lbank

# دریافت داده‌های کندلی
def get_candles(symbol, timeframe='5m', limit=100):
    lbank = create_lbank_client()
    candles = lbank.fetch_ohlcv(symbol, timeframe, limit=limit)
    return candles
