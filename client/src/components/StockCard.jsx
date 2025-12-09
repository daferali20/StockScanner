import React from "react";

export default function StockCard({ stock }) {
  return (
    <div className="border rounded p-3 shadow hover:shadow-lg transition">
      <h2 className="text-xl font-bold">{stock.symbol}</h2>
      <p>Price: ${stock.price}</p>
      {stock.rsi && <p>RSI: {stock.rsi.toFixed(2)}</p>}
      {stock.alert && <p className="text-red-600">{stock.alert}</p>}
    </div>
  );
}

