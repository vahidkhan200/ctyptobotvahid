import pandas as pd

def analyze_symbol(symbol, ohlcv_data):
    if not ohlcv_data or len(ohlcv_data) < 100:
        return [f"دیتای کافی برای {symbol} موجود نیست."]
    
    df = pd.DataFrame(ohlcv_data, columns=["timestamp", "open", "high", "low", "close", "volume"])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

    messages = []

    if detect_double_bottom(df):
        messages.append(f"{symbol}: الگوی کف دوقلو شناسایی شد.")

    if detect_double_top(df):
        messages.append(f"{symbol}: الگوی سقف دوقلو شناسایی شد.")

    if detect_head_and_shoulders(df):
        messages.append(f"{symbol}: الگوی سر و شانه شناسایی شد.")

    if detect_change_of_character(df):
        messages.append(f"{symbol}: چنج آف کاراکتر دیده شد.")

    flag = detect_flag(df)
    if flag:
        messages.append(f"{symbol}: الگوی پرچم {flag} دیده شد.")

    triangle = detect_triangle(df)
    if triangle:
        messages.append(f"{symbol}: مثلث {triangle} مشاهده شد.")

    channel = detect_channel(df)
    if channel:
        messages.append(f"{symbol}: کانال {channel} شناسایی شد.")

    return messages or [f"{symbol}: الگویی شناسایی نشد."]


def detect_double_bottom(df):
    lows = df['low']
    min1 = lows.idxmin()
    range_check = lows[min1+5:min1+30] if min1+30 < len(df) else lows[min1+5:]
    if not range_check.empty:
        min2 = range_check.idxmin()
        if abs(lows[min1] - lows[min2]) / lows[min1] < 0.03:
            return True
    return False

def detect_double_top(df):
    highs = df['high']
    max1 = highs.idxmax()
    range_check = highs[max1+5:max1+30] if max1+30 < len(df) else highs[max1+5:]
    if not range_check.empty:
        max2 = range_check.idxmax()
        if abs(highs[max1] - highs[max2]) / highs[max1] < 0.03:
            return True
    return False

def detect_head_and_shoulders(df):
    highs = df['high'].values
    if len(highs) < 30:
        return False
    for i in range(10, len(highs) - 10):
        left = highs[i - 5:i]
        right = highs[i + 1:i + 6]
        if max(left) < highs[i] and max(right) < highs[i]:
            return True
    return False

def detect_change_of_character(df):
    close = df['close'].values
    for i in range(20, len(close) - 1):
        if close[i] > close[i - 1] and close[i - 1] < close[i - 2]:
            return True
    return False

def detect_flag(df):
    close = df['close']
    if close.iloc[-1] > close.iloc[-10] * 1.05:
        return "صعودی"
    elif close.iloc[-1] < close.iloc[-10] * 0.95:
        return "نزولی"
    return None

def detect_triangle(df):
    highs = df['high']
    lows = df['low']
    if highs.iloc[-1] > highs.iloc[-5] and lows.iloc[-1] > lows.iloc[-5]:
        return "صعودی"
    elif highs.iloc[-1] < highs.iloc[-5] and lows.iloc[-1] < lows.iloc[-5]:
        return "نزولی"
    return None

def detect_channel(df):
    close = df['close']
    if close.is_monotonic_increasing:
        return "صعودی"
    elif close.is_monotonic_decreasing:
        return "نزولی"
    return None
