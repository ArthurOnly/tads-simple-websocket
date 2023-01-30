import asyncio
import websockets

CLIENTS = []

def broadcast(message):
    for websocket in CLIENTS:
        asyncio.create_task(websocket.send(message))

async def recive_handler(websocket):
    async for message in websocket:
        if websocket not in CLIENTS:
            CLIENTS.append(websocket)
            
        if message:
            broadcast(message)

async def main():
    async with websockets.serve(recive_handler, "localhost", 8003):
        await asyncio.Future() 

asyncio.run(main())