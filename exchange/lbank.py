# exchange/lbank.py

import requests
import time
import hashlib
import hmac
from config import LBANK_API_KEY, LBANK_API_SECRET, LBANK_BASE_URL

def sign_params(params):
    sorted_params = sorted(params.items())
    sign_str = '&'.join([f"{k}={v}" for k, v in sorted_params]) + f"&secret_key={LBANK_API_SECRET}"
    sign = hashlib.md5(sign_str.encode('utf-8')).hexdigest().upper()
    params['sign'] = sign
    return params

def get_candles(symbol='btc_usdt', interval='5min', size=100):
    path = '/v1/kline'
    url = LBANK_BASE_URL + path
    params = {
        'symbol': symbol,
        'size': size,
        'type': interval
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()['data']
    else:
        print('Error:', response.text)
        return []
