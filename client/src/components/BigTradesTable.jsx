import React from "react";

export default function BigTradesTable({ trades }) {
  return (
    <table className="min-w-full table-auto border-collapse border border-gray-300">
      <thead>
        <tr className="bg-gray-200">
          <th className="border px-2 py-1">Symbol</th>
          <th className="border px-2 py-1">Price</th>
          <th className="border px-2 py-1">Volume</th>
          <th className="border px-2 py-1">Change%</th>
          <th className="border px-2 py-1">Alert</th>
        </tr>
      </thead>
      <tbody>
        {trades.map((t, i) => (
          <tr key={i}>
            <td className="border px-2 py-1">{t.symbol}</td>
            <td className="border px-2 py-1">{t.price}</td>
            <td className="border px-2 py-1">{t.volume}</td>
            <td className="border px-2 py-1">{t.change?.toFixed(2)}</td>
            <td className="border px-2 py-1 text-red-600">{t.alert}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

