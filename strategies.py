def analyze_symbol(symbol, ohlcv_data):
    """
    تحلیل ساده برای تست اولیه. بعداً الگوریتم‌ کامل رو اضافه می‌کنیم.
    
    :param symbol: نماد ارز (مثلاً BTC_USDT)
    :param ohlcv_data: لیست داده‌های کندل‌ها (Open, High, Low, Close, Volume)
    :return: لیستی از سیگنال‌ها یا پیام‌ها برای ارسال به تلگرام
    """
    # فقط چک می‌کنیم دیتا دریافت شده
    if not ohlcv_data or len(ohlcv_data) < 50:
        return [f"دیتای کافی برای {symbol} موجود نیست."]
    
    # اینجا جای تحلیل‌ تکنیکال‌ آینده است
    return [f"بررسی {symbol} انجام شد. (تست)"]
