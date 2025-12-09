import openai
from config import OPENAI_API_KEY
openai.api_key = OPENAI_API_KEY

def analyze_stock(symbol, data):
    """
    تحليل السهم باستخدام GPT.
    data: dict يحتوي على السعر، RSI، MACD، SMA50، SMA200، حجم التداول
    """
    prompt = f"""
    حلل السهم {symbol} بناءً على:
    السعر: {data.get('price',0)}
    RSI: {data.get('rsi',0)}
    MACD: {data.get('macd',0)}
    SMA50: {data.get('sma50',0)}
    SMA200: {data.get('sma200',0)}
    الحجم: {data.get('volume',0)}

    اعطني:
    - اتجاه السهم (صاعد/هابط/محايد)
    - مناطق الدخول
    - وقف الخسارة
    - جني الأرباح
    - مستوى الخطورة
    """

    response = openai.ChatCompletion.create(
        model="gpt-5",
        messages=[{"role":"user","content":prompt}]
    )
    return response.choices[0].message.content
