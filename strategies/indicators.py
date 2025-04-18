import ccxt
import pandas as pd
import ta

exchange = ccxt.lbank()

def get_ohlcv(symbol, timeframe, limit=100):
    data = exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
    df = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    return df

def get_indicators(symbol, timeframe):
    df = get_ohlcv(symbol, timeframe)
    df['rsi'] = ta.momentum.RSIIndicator(df['close']).rsi()
    df['macd'] = ta.trend.MACD(df['close']).macd_diff()
    df['ema50'] = ta.trend.EMAIndicator(df['close'], window=50).ema_indicator()
    df['atr'] = ta.volatility.AverageTrueRange(df['high'], df['low'], df['close']).average_true_range()

    signal = []
    if df['rsi'].iloc[-1] < 30:
        signal.append("RSI در ناحیه اشباع فروش")
    if df['macd'].iloc[-1] > 0 and df['macd'].iloc[-2] < 0:
        signal.append("تقاطع صعودی MACD")
    if df['close'].iloc[-1] > df['ema50'].iloc[-1]:
        signal.append("قیمت بالای EMA50")

    return "\n".join(signal) if signal else None
