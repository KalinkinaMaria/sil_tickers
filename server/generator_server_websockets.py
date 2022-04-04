"""
Websocket server for generating tickers price. 
Server is waiting clients and when client connected server initialise price for 100 tickers and send it to client. 
Then server updates prices and send it to client once per second.
"""

import json
import signal
import asyncio
import logging
from random import random

import websockets

logging.basicConfig(level=logging.INFO)

WS_HOST = '' #"localhost"
WS_PORT = 8764

def generate_movement() -> int:
    """Generate price changing."""
    movement = -1 if random() < 0.5 else 1
    return movement

def next_tickets(tickets_dict: dict) -> dict:
    """Generate new tickers prices.

    Keyword arguments:
    tickets_dict -- dict with previos tickers prices

    """
    return {i:tickets_dict[i] + generate_movement() for i in tickets_dict.keys()}

def init_tickets() -> dict:
    """Initialization 100 tickers prices."""
    return { f'ticker_{i:02}':0 for i in range(100) }

async def on_connect(ws: websockets.WebSocketServer) -> None:
    """Asynchronous handler function - waiting clients and infinite cycle for generation new prices and sending it to clients.

    Keyword arguments:
    ws -- websocker server 

    """
    logging.info(f"<<< Connection {ws.id}: Opened")

    tickets = init_tickets()

    while True:
        try:
            await ws.send(json.dumps(tickets))
            logging.info(f">>> Connection {ws.id}: Tickers sent")

            await asyncio.sleep(1)

            tickets = next_tickets(tickets)
        except websockets.exceptions.ConnectionClosedOK:
            logging.info(f"<<< Connection {ws.id}: Closed")
            break
        except websockets.exceptions.WebSocketException as e:
            logging.error(f"<<< Connection {ws.id}: Error recieved {str(e)}")
            break

async def main():
    """Creation websocket and starting loop."""
    async with websockets.serve(on_connect, WS_HOST, WS_PORT):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
else:
    loop = asyncio.get_event_loop()

    start_server = websockets.serve(on_connect, WS_HOST, WS_PORT)
    server = loop.run_until_complete(start_server)

    stop = asyncio.Future()
    loop.add_signal_handler(signal.SIGTERM, stop.set_result, None)
    loop.run_until_complete(stop)

    server.close()
    loop.run_until_complete(server.wait_closed())
