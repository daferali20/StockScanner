import os

# إعدادات قاعدة البيانات
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", 5432))
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS", "password")
DB_NAME = os.getenv("DB_NAME", "stock_scanner")

# إعدادات OpenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "ضع_مفتاحك_هنا")

# إعدادات WebSocket
WS_PORT = int(os.getenv("WS_PORT", 8765))
