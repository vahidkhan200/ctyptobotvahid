import numpy as np

def is_flag_pattern(candles):
    closes = np.array([c[4] for c in candles])  # فقط قیمت پایانی
    highs = np.array([c[2] for c in candles])
    lows = np.array([c[3] for c in candles])

    last = closes[-1]
    trend = closes[-15:-5]

    # بررسی روند اولیه (مثلاً ۱۰ کندل قبل از consolidation)
    if trend[-1] < trend[0]:
        return False, None  # پرچم نیاز به روند اولیه داره

    # consolidation: نوسان محدود در چند کندل آخر
    cons_high = np.max(highs[-5:])
    cons_low = np.min(lows[-5:])
    if (cons_high - cons_low) / cons_low < 0.02:
        return True, "پرچم صعودی احتمالی"

    return False, None
