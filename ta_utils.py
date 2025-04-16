import pandas as pd

def is_buy_signal(df):
    df['MA5'] = df['close'].rolling(window=5).mean()
    df['MA20'] = df['close'].rolling(window=20).mean()
    
    if len(df) < 21:
        return False
    
    return df['MA5'].iloc[-2] < df['MA20'].iloc[-2] and df['MA5'].iloc[-1] > df['MA20'].iloc[-1]
