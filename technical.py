import requests
import pandas as pd

def fetch_ohlcv(symbol, interval='15min', limit=100):
    url = f"https://api.lbank.info/v1/kline.do?symbol={symbol}&size={limit}&type={interval}"
    try:
        response = requests.get(url)
        data = response.json()
        if data['result'] and 'data' in data:
            df = pd.DataFrame(data['data'], columns=[
                'timestamp', 'open', 'high', 'low', 'close', 'volume'
            ])
            df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
            df = df.astype({
                'open': float, 'high': float, 'low': float, 'close': float, 'volume': float
            })
            return df
        else:
            return None
    except Exception as e:
        print(f"Error fetching OHLCV data for {symbol}: {e}")
        return None

def analyze_market(df):
    if df is None or len(df) < 20:
        return None

    # تحلیل تکنیکال ساده - میانگین متحرک
    df['ma7'] = df['close'].rolling(window=7).mean()
    df['ma20'] = df['close'].rolling(window=20).mean()

    if df['ma7'].iloc[-2] < df['ma20'].iloc[-2] and df['ma7'].iloc[-1] > df['ma20'].iloc[-1]:
        return "کراس صعودی اتفاق افتاده (سیگنال خرید)"
    elif df['ma7'].iloc[-2] > df['ma20'].iloc[-2] and df['ma7'].iloc[-1] < df['ma20'].iloc[-1]:
        return "کراس نزولی اتفاق افتاده (سیگنال فروش)"
    else:
        return None
