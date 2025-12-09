import React, { useEffect, useState } from "react";
import { connectWebSocket } from "../websocket";
import StockCard from "../components/StockCard";
import BigTradesTable from "../components/BigTradesTable";
import AIAssistant from "../components/AIAssistant";

export default function Dashboard() {
  const [stocks, setStocks] = useState([]);
  const [trades, setTrades] = useState([]);

  useEffect(() => {
    connectWebSocket((data) => {
      // تحديث قائمة الأسهم
      setStocks((prev) => {
        const index = prev.findIndex((s) => s.symbol === data.symbol);
        if (index >= 0) {
          const copy = [...prev];
          copy[index] = data;
          return copy;
        } else {
          return [...prev, data];
        }
      });

      // إضافة إلى BigTrades إذا الحجم كبير
      if (data.volume > 1000) {
        setTrades((prev) => [...prev.filter(t => t.symbol !== data.symbol), data]);
      }
    });
  }, []);

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">Live Stock Scanner</h1>
      <AIAssistant stockData={stocks} />
      <div className="grid grid-cols-4 gap-4 my-4">
        {stocks.map((s) => (
          <StockCard key={s.symbol} stock={s} />
        ))}
      </div>
      <h2 className="text-xl font-bold my-2">Big Trades</h2>
      <BigTradesTable trades={trades} />
    </div>
  );
}

