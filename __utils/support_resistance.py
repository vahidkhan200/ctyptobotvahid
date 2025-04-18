# utils/support_resistance.py

def detect_support_resistance(df, window=20):
    recent_high = df['high'].rolling(window).max().iloc[-1]
    recent_low = df['low'].rolling(window).min().iloc[-1]
    return round(recent_low, 4), round(recent_high, 4)
