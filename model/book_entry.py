class BookEntry():

    is_valid = False

    stream_key = 'stream'
    data_key = 'data'
    order_book_updateId_key = 'u'
    traiding_symbol_key = 's'
    best_bid_price_key = 'b'
    best_bid_qty_key = 'B'
    best_ask_price_key = 'a'
    best_ask_qty_key = 'A'

    stream = ''
    order_book_updateId = int
    traiding_symbol = ''
    best_bid_price = ''
    best_bid_qty = ''
    best_ask_price = ''
    best_ask_qty = ''

    def __init__(self, payload):
        self._transform(payload)
    
    def _transform(self, payload):
        if self.stream_key in payload.keys() and self.data_key in payload.keys():
            self.is_valid = True
            self.stream = payload[self.stream_key]
            data = payload[self.data_key]
            if self.order_book_updateId_key in data.keys():
                self.order_book_updateId = data[self.order_book_updateId_key]
            if self.traiding_symbol_key in data.keys():
                self.traiding_symbol = data[self.traiding_symbol_key]
            if self.best_bid_price_key in data.keys():
                self.best_bid_price = data[self.best_bid_price_key]
            if self.best_bid_qty_key in data.keys():
                self.best_bid_qty = data[self.best_bid_qty_key]
            if self.best_ask_price_key in data.keys():
                self.best_ask_price = data[self.best_ask_price_key]
            if self.best_ask_qty_key in data.keys():
                self.best_ask_qty = data[self.best_ask_qty_key]
            
    def __str__(self):
        return f"is_valid={self.is_valid}, stream={self.stream}, order_book_updateId={self.order_book_updateId}, traiding_symbol={self.traiding_symbol}, best_bid_price={self.best_bid_price}, best_bid_qty={self.best_bid_qty}, best_ask_price={self.best_ask_price}, best_ask_qty={self.best_ask_qty}"

# book_tick = {'stream': 'ethusdt@bookTicker', 'data': {'u': 12134831560, 's': 'ETHUSDT', 'b': '4387.42000000', 'B': '6.23450000', 'a': '4387.43000000', 'A': '1.62630000'}}
# book_entry = BookEntry(book_tick)
# print(book_entry)

# Documentation
# https://github.com/binance/binance-spot-api-docs/blob/master/web-socket-streams.md#:~:text=%7B%0A%20%20%22u%22%3A400900217%2C%20%20%20%20%20//%20order%20book%20updateId%0A%20%20%22s%22%3A%22BNBUSDT%22%2C%20%20%20%20%20//%20symbol%0A%20%20%22b%22%3A%2225.35190000%22%2C%20//%20best%20bid%20price%0A%20%20%22B%22%3A%2231.21000000%22%2C%20//%20best%20bid%20qty%0A%20%20%22a%22%3A%2225.36520000%22%2C%20//%20best%20ask%20price%0A%20%20%22A%22%3A%2240.66000000%22%20%20//%20best%20ask%20qty%0A%7D
