# signal.py

def generate_signal(df):
    if df is None or df.empty:
        return None

    latest = df.iloc[-1]

    signal = None

    # مثال: اگر RSI کمتر از 30 و MACD کراس به بالا زده باشه = سیگنال خرید
    if latest['rsi'] < 30 and latest['macd'] > latest['signal']:
        signal = 'buy'

    # اگر RSI بالاتر از 70 و MACD کراس به پایین زده باشه = سیگنال فروش
    elif latest['rsi'] > 70 and latest['macd'] < latest['signal']:
        signal = 'sell'

    return signal
