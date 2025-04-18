import ccxt
import time
import pandas as pd
from telegram_bot import send_telegram_message
from strategies import analyze_symbol

exchange = ccxt.binance()
symbols = [
    'BTC/USDT', 'ETH/USDT', 'BNB/USDT', 'SOL/USDT',
    'XRP/USDT', 'ADA/USDT', 'DOGE/USDT', 'DOT/USDT'
]

def fetch_ohlcv(symbol, timeframe='1h', limit=100):
    data = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
    df = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    return df

while True:
    for symbol in symbols:
        try:
            df = fetch_ohlcv(symbol)
            signals = analyze_symbol(symbol, df)

            if signals:
                message = f"📊 **تحلیل تکنیکال {symbol}**\n\n"
                for signal in signals:
                    message += f"• {signal}\n"
                send_telegram_message(message)

        except Exception as e:
            print(f"Error with {symbol}: {e}")

    time.sleep(60 * 60)  # اجرای تحلیل هر ۱ ساعت
