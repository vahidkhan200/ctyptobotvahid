from strategies.indicators import get_indicators
from strategies.price_action import detect_price_action
from strategies.chart_patterns import detect_chart_patterns

def analyze_symbol(symbol, timeframe):
    try:
        results = []
        indicators = get_indicators(symbol, timeframe)
        price_action = detect_price_action(symbol, timeframe)
        patterns = detect_chart_patterns(symbol, timeframe)

        if indicators:
            results.append(indicators)
        if price_action:
            results.append(price_action)
        if patterns:
            results.append(patterns)

        if results:
            return f"سیگنال برای {symbol} در تایم {timeframe}:\n\n" + "\n".join(results)
    except Exception as e:
        print(f"خطا در بررسی {symbol} | {timeframe} -> {e}")
    return None
