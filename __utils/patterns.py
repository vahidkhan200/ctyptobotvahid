# utils/patterns.py

import talib

def detect_candlestick_patterns(df):
    patterns = {
        "Hammer": talib.CDLHAMMER,
        "Engulfing": talib.CDLENGULFING,
        "Morning Star": talib.CDLMORNINGSTAR,
        "Doji": talib.CDLDOJI,
        "Shooting Star": talib.CDLSHOOTINGSTAR,
        "Evening Star": talib.CDLEVENINGSTAR,
        "Harami": talib.CDLHARAMI
    }

    detected = []
    for name, func in patterns.items():
        result = func(df['open'], df['high'], df['low'], df['close'])
        if result.iloc[-1] != 0:
            detected.append(name)
    return ", ".join(detected) if detected else None

def detect_chart_patterns(df):
    close = df['close']
    if close.iloc[-1] > close.iloc[-2] > close.iloc[-3] and close.iloc[-1] > close.iloc[-4]:
        return "کف دوقلو"
    if close.iloc[-1] < close.iloc[-2] < close.iloc[-3] and close.iloc[-1] < close.iloc[-4]:
        return "سقف دوقلو"
    # می‌تونی اینجا الگوهای مثلث و کانال هم اضافه کنی به صورت شرط‌های ساده
    return None
