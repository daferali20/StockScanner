import React, { useState } from "react";

export default function AIAssistant({ stockData }) {
  const [symbol, setSymbol] = useState("");
  const [analysis, setAnalysis] = useState("");

  const handleAnalyze = async () => {
    try {
      const res = await fetch(`http://localhost:8000/analyze/${symbol}`);
      const data = await res.json();
      setAnalysis(data.analysis);
    } catch (err) {
      setAnalysis("Error fetching analysis");
    }
  };

  return (
    <div className="border rounded p-3 shadow my-2">
      <input
        type="text"
        placeholder="Enter Symbol"
        value={symbol}
        onChange={(e) => setSymbol(e.target.value)}
        className="border px-2 py-1 mr-2"
      />
      <button
        onClick={handleAnalyze}
        className="bg-blue-500 text-white px-3 py-1 rounded"
      >
        Analyze
      </button>
      {analysis && <p className="mt-2 whitespace-pre-wrap">{analysis}</p>}
    </div>
  );
}

