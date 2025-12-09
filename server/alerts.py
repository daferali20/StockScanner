from database import get_connection
import asyncio
from websocket_manager import broadcast

def check_alerts(data):
    """
    فحص إذا كان السهم يستحق تنبيه
    مثال: RSI < 30 (شراء) أو RSI > 70 (بيع)
    """
    symbol = data.get("symbol")
    rsi = data.get("rsi", 50)
    message = None

    if rsi < 30:
        message = f"{symbol} Oversold! Consider Buying."
    elif rsi > 70:
        message = f"{symbol} Overbought! Consider Selling."

    if message:
        # حفظ التنبيه في DB
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO alerts(symbol, message)
            VALUES(%s,%s)
        """, (symbol, message))
        conn.commit()
        cur.close()
        conn.close()

        # إرسال التنبيه للواجهة
        asyncio.create_task(broadcast({"symbol": symbol, "alert": message}))

