import pandas as pd
import numpy as np

def analyze_symbol(ohlcv):
    df = pd.DataFrame(ohlcv, columns=["timestamp", "open", "high", "low", "close", "volume"])
    df['rsi'] = compute_rsi(df['close'])

    if df['rsi'].iloc[-1] < 30:
        return "احتمال بازگشت صعودی (RSI پایین)"
    elif df['rsi'].iloc[-1] > 70:
        return "احتمال اصلاح نزولی (RSI بالا)"
    else:
        return None

def compute_rsi(series, period=14):
    delta = series.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))
