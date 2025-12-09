import asyncio
import websockets
import json

# قائمة العملاء المتصلين
connected_clients = set()

async def register_client(websocket):
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            pass  # لا نتلقى رسائل من العميل الآن
    finally:
        connected_clients.remove(websocket)

async def broadcast(message: dict):
    if connected_clients:
        data = json.dumps(message)
        await asyncio.wait([client.send(data) for client in connected_clients])

async def start_server(host="0.0.0.0", port=8765):
    async with websockets.serve(register_client, host, port):
        print(f"[WS] Server running on ws://{host}:{port}")
        await asyncio.Future()  # run forever

# لتشغيل الخادم مباشرة
if __name__ == "__main__":
    asyncio.run(start_server())

