import time
from config.general import TRAIDING_SYMBOLS
from binance.websocket.spot.websocket_client import SpotWebsocketClient

spot_websocket_client = SpotWebsocketClient()
callback = None
book_list = [f"{ts.lower()}@bookTicker" for ts in TRAIDING_SYMBOLS]

def subscribe():
    spot_websocket_client.instant_subscribe(
            stream=book_list,
            callback=callback,
    )

def subscribe2():
    # Live subscription
    spot_websocket_client.ticker(
        symbol="ethbtc",
        id=1,
        callback=spot_websocket_client,
    )

print(book_list)