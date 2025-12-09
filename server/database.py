import psycopg2
from config import DB_HOST, DB_PORT, DB_USER, DB_PASS, DB_NAME

def get_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASS,
        dbname=DB_NAME
    )
    return conn

def init_db():
    conn = get_connection()
    cur = conn.cursor()
    # إنشاء جدول للأسهم
    cur.execute("""
    CREATE TABLE IF NOT EXISTS stocks_prices (
        id SERIAL PRIMARY KEY,
        symbol VARCHAR(20),
        price NUMERIC,
        volume BIGINT,
        rsi NUMERIC,
        macd NUMERIC,
        sma50 NUMERIC,
        sma200 NUMERIC,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)
    # جدول التنبيهات
    cur.execute("""
    CREATE TABLE IF NOT EXISTS alerts (
        id SERIAL PRIMARY KEY,
        symbol VARCHAR(20),
        message TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)
    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    init_db()
