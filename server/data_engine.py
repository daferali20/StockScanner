import requests
import pandas as pd
from indicators import calculate_indicators
from database import get_connection
import asyncio
from websocket_manager import broadcast

API_KEY = "ضع_مفتاح_API_هنا"
BASE_URL = "https://finnhub.io/api/v1"

def fetch_stock_data(symbol):
    """ جلب آخر أسعار السهم من Finnhub """
    url = f"{BASE_URL}/quote?symbol={symbol}&token={API_KEY}"
    resp = requests.get(url)
    if resp.status_code == 200:
        data = resp.json()
        return {
            "symbol": symbol,
            "price": data.get("c"),
            "open": data.get("o"),
            "high": data.get("h"),
            "low": data.get("l"),
            "prev_close": data.get("pc"),
            "volume": data.get("v")
        }
    return None

def save_to_db(data):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO stocks_prices(symbol, price, volume)
        VALUES(%s,%s,%s)
    """, (data['symbol'], data['price'], data['volume']))
    conn.commit()
    cur.close()
    conn.close()

async def update_stocks(symbols):
    """ تحديث مستمر وإرسال للواجهة """
    while True:
        for symbol in symbols:
            data = fetch_stock_data(symbol)
            if data:
                save_to_db(data)
                await broadcast(data)
        await asyncio.sleep(2)  # تحديث كل ثانيتين

