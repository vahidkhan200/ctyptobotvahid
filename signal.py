# signal.py

def generate_signal(df):
    latest = df.iloc[-1]

    signals = []

    # سیگنال خرید بر اساس MACD کراس
    if latest['MACD'] > latest['MACD_signal'] and df.iloc[-2]['MACD'] < df.iloc[-2]['MACD_signal']:
        signals.append("MACD: Buy")

    # سیگنال فروش MACD
    if latest['MACD'] < latest['MACD_signal'] and df.iloc[-2]['MACD'] > df.iloc[-2]['MACD_signal']:
        signals.append("MACD: Sell")

    # سیگنال خرید بر اساس RSI
    if latest['RSI'] < 30:
        signals.append("RSI: Oversold (Buy)")
    elif latest['RSI'] > 70:
        signals.append("RSI: Overbought (Sell)")

    # کراس قیمت و EMA
    if latest['close'] > latest['EMA_20'] and df.iloc[-2]['close'] <= df.iloc[-2]['EMA_20']:
        signals.append("Price crossed above EMA20 (Buy)")
    elif latest['close'] < latest['EMA_20'] and df.iloc[-2]['close'] >= df.iloc[-2]['EMA_20']:
        signals.append("Price crossed below EMA20 (Sell)")

    return signals
