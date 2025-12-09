# StockScanner
StockScanner/
│
├─ client/                  # واجهة المستخدم (React)
│   ├─ src/
│   │   ├─ components/
│   │   │   ├─ BigTradesTable.jsx
│   │   │   ├─ StockCard.jsx
│   │   │   ├─ ChartView.jsx
│   │   │   └─ AIAssistant.jsx
│   │   ├─ pages/
│   │   │   └─ Dashboard.jsx
│   │   └─ websocket.js
│   └─ package.json
│
├─ server/                  # الخادم
│   ├─ main.py
│   ├─ websocket_manager.py
│   ├─ ai_engine.py
│   ├─ data_engine.py
│   ├─ indicators.py
│   ├─ alerts.py
│   ├─ database.py
│   └─ config.py
│
├─ requirements.txt
└─ README.md
