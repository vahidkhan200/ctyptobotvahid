import talib

def calculate_indicators(df):
    df['EMA20'] = talib.EMA(df['Close'], timeperiod=20)
    df['EMA50'] = talib.EMA(df['Close'], timeperiod=50)
    macd, macdsignal, macdhist = talib.MACD(df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
    df['MACD'] = macd
    df['MACD_Signal'] = macdsignal
    df['MACD_Hist'] = macdhist
    df['RSI'] = talib.RSI(df['Close'], timeperiod=14)
    df['ATR'] = talib.ATR(df['High'], df['Low'], df['Close'], timeperiod=14)
    return df
