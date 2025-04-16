# lbank_api.py

import requests
import pandas as pd
from config import LBANK_API_URL

def get_ohlcv(symbol, interval='15min', limit=100):
    endpoint = f"{LBANK_API_URL}/v1/kline"
    params = {
        'symbol': symbol,
        'size': limit,
        'type': interval
    }
    try:
        response = requests.get(endpoint, params=params)
        data = response.json()

        if data['result'] != 'true':
            raise Exception(f"API error: {data}")

        kline_data = data['data']
        df = pd.DataFrame(kline_data, columns=[
            'timestamp', 'open', 'high', 'low', 'close', 'volume'
        ])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        df[['open', 'high', 'low', 'close', 'volume']] = df[['open', 'high', 'low', 'close', 'volume']].astype(float)
        return df

    except Exception as e:
        print(f"Error fetching OHLCV data for {symbol}: {e}")
        return pd.DataFrame()
