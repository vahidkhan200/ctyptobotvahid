import pandas as pd
import numpy as np

def detect_double_bottom(df):
    bottoms = []
    for i in range(2, len(df) - 2):
        if df['low'][i] < df['low'][i-1] and df['low'][i] < df['low'][i+1]:
            if abs(df['low'][i] - df['low'][i-2]) / df['low'][i] < 0.01:
                bottoms.append((i-2, i))
    return bottoms

def detect_double_top(df):
    tops = []
    for i in range(2, len(df) - 2):
        if df['high'][i] > df['high'][i-1] and df['high'][i] > df['high'][i+1]:
            if abs(df['high'][i] - df['high'][i-2]) / df['high'][i] < 0.01:
                tops.append((i-2, i))
    return tops

def detect_head_and_shoulders(df):
    patterns = []
    for i in range(3, len(df) - 3):
        left = df['high'][i-2]
        head = df['high'][i]
        right = df['high'][i+2]
        if head > left and head > right and abs(left - right) / head < 0.03:
            patterns.append(i)
    return patterns

def detect_change_of_character(df):
    # ChoCH = شکست سقف یا کف قبلی
    chochs = []
    for i in range(2, len(df)):
        if df['high'][i] > max(df['high'][i-2:i]) and df['low'][i] < min(df['low'][i-2:i]):
            chochs.append(i)
    return chochs

def detect_patterns(df):
    return {
        "double_bottom": detect_double_bottom(df),
        "double_top": detect_double_top(df),
        "head_and_shoulders": detect_head_and_shoulders(df),
        "change_of_character": detect_change_of_character(df),
    }
