# indicators.py

import ta

def add_indicators(df):
    # EMA (مثلاً برای 20 کندل آخر)
    df['EMA_20'] = ta.trend.ema_indicator(df['close'], window=20).ema_indicator()

    # RSI
    df['RSI'] = ta.momentum.RSIIndicator(df['close'], window=14).rsi()

    # MACD
    macd = ta.trend.MACD(df['close'])
    df['MACD'] = macd.macd()
    df['MACD_signal'] = macd.macd_signal()

    # ATR
    atr = ta.volatility.AverageTrueRange(high=df['high'], low=df['low'], close=df['close'], window=14)
    df['ATR'] = atr.average_true_range()

    return df
