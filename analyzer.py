import ccxt
from utils.indicators import analyze_with_indicators

symbols = ["BTC/USDT", "ETH/USDT"]
timeframes = ["1h", "4h"]

def analyze_all_symbols():
    exchange = ccxt.binance()
    signals = []
    for symbol in symbols:
        for tf in timeframes:
            ohlcv = exchange.fetch_ohlcv(symbol, timeframe=tf, limit=100)
            signal = analyze_with_indicators(symbol, tf, ohlcv)
            if signal:
                signals.append(signal)
    return signals
