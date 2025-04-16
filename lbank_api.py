# lbank_api.py

import requests
import pandas as pd
from config import LBANK_API_URL

def get_ohlcv(symbol='btc_usdt', interval='15min', limit=100):
    params = {
        'symbol': symbol,
        'size': limit,
        'type': interval
    }
    response = requests.get(LBANK_API_URL, params=params)
    data = response.json()['data']

    df = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
    df = df.astype({
        'open': 'float',
        'high': 'float',
        'low': 'float',
        'close': 'float',
        'volume': 'float'
    })
    return df
