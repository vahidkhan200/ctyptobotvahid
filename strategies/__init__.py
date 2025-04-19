# strategies/__init__.py

def analyze_symbol(symbol_data):
    # تحلیل نمونه‌ای (مثل همون که در بالا گفتم)
    try:
        klines = symbol_data.get('klines', [])
        symbol = symbol_data.get('symbol', 'UNKNOWN')

        if len(klines) < 2:
            return {'symbol': symbol, 'signal': 'hold'}

        last_close = float(klines[-1][4])
        prev_close = float(klines[-2][4])

        if last_close > prev_close * 1.01:
            signal = 'buy'
        elif last_close < prev_close * 0.99:
            signal = 'sell'
        else:
            signal = 'hold'

        return {'symbol': symbol, 'signal': signal}

    except Exception as e:
        return {'symbol': symbol_data.get('symbol', 'UNKNOWN'), 'signal': 'error', 'error': str(e)}
