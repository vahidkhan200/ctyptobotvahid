import requests
from config import LBANK_API_URL

def get_symbols():
    url = f"{LBANK_API_URL}/v2/currencyPairs.do"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return [item['symbol'] for item in data.get('data', [])]
    return []

def get_klines(symbol, interval="1min", size=100):
    url = f"{LBANK_API_URL}/v1/kline.do"
    params = {
        "symbol": symbol,
        "type": interval,
        "size": size
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    return []
