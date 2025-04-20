import time
from exchange.lbank import get_candles
from analysis.chart_patterns import double_top_bottom
from signal.telegram import send_signal
from utils.helpers import wait_for_next_candle

def main():
    while True:
        candles = get_candles('BTC/USDT', '5m', limit=100)
        
        # بررسی الگوها
        if double_top_bottom(candles):
            send_signal('BTCUSDT', 'لانگ', 40000, 40500, 41000, 39500, 'x10', 'Double Top')
        
        # سایر الگوها رو هم به همین صورت بررسی کن

        wait_for_next_candle('5m')  # به مدت 5 دقیقه صبر کن

if __name__ == '__main__':
    main()
