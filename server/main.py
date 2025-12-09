import asyncio
from server.websocket_manager import start_server, broadcast
from server.data_engine import update_stocks, fetch_stock_data, save_to_db
from server.indicators import calculate_indicators
from server.ai_engine import analyze_stock
from server.alerts import check_alerts
from server.database import init_db

# قائمة الأسهم التي تريد مراقبتها
WATCHLIST = ["AAPL", "TSLA", "MSFT", "AMZN", "NVDA"]

async def process_stock(symbol):
    while True:
        # 1️⃣ جلب البيانات
        data = fetch_stock_data(symbol)
        if data:
            # 2️⃣ حفظ الأسعار في DB
            save_to_db(data)

            # 3️⃣ تحليل المؤشرات الفنية
            df = calculate_indicators(pd.DataFrame([data]))
            indicators = df.iloc[0].to_dict()
            data.update(indicators)

            # 4️⃣ تحليل AI لكل سهم
            try:
                ai_result = analyze_stock(symbol, data)
                data["ai_analysis"] = ai_result
            except Exception as e:
                data["ai_analysis"] = f"AI analysis failed: {e}"

            # 5️⃣ فحص التنبيهات
            check_alerts(data)

            # 6️⃣ إرسال البيانات للواجهة
            await broadcast(data)

        await asyncio.sleep(2)  # تحديث كل ثانيتين

async def main():
    # تهيئة قاعدة البيانات
    init_db()
    print("[DB] Database initialized.")

    # تشغيل WebSocket
    asyncio.create_task(start_server())

    # تشغيل مراقبة الأسهم لكل سهم في Watchlist
    tasks = [asyncio.create_task(process_stock(symbol)) for symbol in WATCHLIST]

    await asyncio.gather(*tasks)

if __name__ == "__main__":
    import pandas as pd
    asyncio.run(main())

