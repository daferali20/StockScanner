import streamlit as st
import time
import pandas as pd

st.set_page_config(page_title="Stock Scanner", layout="wide")

st.title("🚀 أفضل الأسهم صعودًا – تحديث تلقائي")

# دالة وهمية لجلب بيانات الأسهم
def get_top_movers():
    return [
        {"symbol": "AAPL", "change": 3.5, "volume": 12000000},
        {"symbol": "NVDA", "change": 2.9, "volume": 9800000},
        {"symbol": "TSLA", "change": 2.4, "volume": 15000000},
    ]

placeholder = st.empty()

while True:
    stocks = get_top_movers()
    df = pd.DataFrame(stocks)
    placeholder.table(df)
    time.sleep(5)
