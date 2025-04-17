import matplotlib.pyplot as plt
import pandas as pd
import os

def draw_candlestick_chart(df, symbol, timeframe):
    plt.figure(figsize=(12, 6))
    plt.title(f'{symbol.upper()} - {timeframe} - آخرین ۱۰۰ کندل')

    # رسم کندل‌ها
    for i in range(len(df)):
        color = 'green' if df['close'][i] >= df['open'][i] else 'red'
        plt.plot([i, i], [df['low'][i], df['high'][i]], color=color)  # خط بالا پایین
        plt.plot([i, i], [df['open'][i], df['close'][i]], linewidth=6, color=color)  # بدنه کندل

    plt.xticks([])  # پنهان کردن محور X
    plt.tight_layout()

    # مسیر ذخیره‌سازی
    folder = 'charts'
    os.makedirs(folder, exist_ok=True)
    file_path = f'{folder}/{symbol}_{timeframe}.png'
    plt.savefig(file_path)
    plt.close()
    return file_path
