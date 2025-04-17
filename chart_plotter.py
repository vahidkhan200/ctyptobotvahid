import matplotlib.pyplot as plt
import pandas as pd
import os

def plot_candles_with_patterns(df, symbol, patterns, timeframe='1h'):
    plt.figure(figsize=(12, 6))
    plt.title(f"{symbol.upper()} | {timeframe} Chart with Patterns")
    plt.plot(df['close'].values, label='Close Price', color='black')

    # Double Bottom
    for idx_pair in patterns.get("double_bottom", []):
        for idx in idx_pair:
            plt.scatter(idx, df['low'][idx], color='green', label='Double Bottom')

    # Double Top
    for idx_pair in patterns.get("double_top", []):
        for idx in idx_pair:
            plt.scatter(idx, df['high'][idx], color='red', label='Double Top')

    # Head and Shoulders
    for idx in patterns.get("head_and_shoulders", []):
        plt.scatter(idx, df['high'][idx], color='blue', label='Head & Shoulders')

    # Change of Character
    for idx in patterns.get("change_of_character", []):
        plt.axvline(x=idx, linestyle='--', color='purple', label='ChoCH')

    plt.legend(loc='upper left')
    filename = f"{symbol}_{timeframe}_chart.png"
    filepath = os.path.join("/tmp", filename)
    plt.savefig(filepath)
    plt.close()
    return filepath
