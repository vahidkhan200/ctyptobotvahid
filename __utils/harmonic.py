# utils/harmonic.py

def detect_harmonic_patterns(df):
    # الگوریتم دقیق نیاز به تشخیص PRZ و نقاط XABCD دارد
    # ولی در اینجا یک نسخه فرضی ساده‌شده می‌گذاریم
    high = df['high']
    low = df['low']

    last_move = high.iloc[-1] - low.iloc[-1]
    if abs(last_move) > (high.max() - low.min()) * 0.618:
        return "احتمال الگوی گارتلی یا بت"

    return None
