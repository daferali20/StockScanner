let ws;

export function connectWebSocket(onMessage) {
  ws = new WebSocket("ws://localhost:8765");

  ws.onopen = () => {
    console.log("WebSocket connected");
  };

  ws.onmessage = (event) => {
    const data = JSON.parse(event.data);
    onMessage(data);
  };

  ws.onclose = () => {
    console.log("WebSocket disconnected, reconnecting in 3s...");
    setTimeout(() => connectWebSocket(onMessage), 3000);
  };
}

