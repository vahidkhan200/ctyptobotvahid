import requests

def get_symbols():
    url = "https://api.lbkex.com/v2/ticker/24hr.do"
    
    # درخواست به API
    response = requests.get(url)
    
    # بررسی وضعیت پاسخ
    if response.status_code == 200:
        # تبدیل پاسخ به دیکشنری JSON
        data = response.json()
        
        # بررسی وجود داده‌ها در پاسخ
        if 'data' in data:
            # استخراج نمادها از داده‌ها
            return [item['symbol'] for item in data['data']]
        else:
            print("داده 'data' در پاسخ یافت نشد.")
            return []
    else:
        print(f"خطا در دریافت داده‌ها. کد وضعیت: {response.status_code}")
        return []
