import talib

def detect_candlestick_patterns(df):
    patterns = []
    for i in range(len(df)):
        pattern = 'none'
        if talib.CDLHAMMER(df['Open'], df['High'], df['Low'], df['Close'])[i] != 0:
            pattern = 'bullish'
        elif talib.CDLHANGINGMAN(df['Open'], df['High'], df['Low'], df['Close'])[i] != 0:
            pattern = 'bearish'
        patterns.append(pattern)
    return patterns
