from itertools import permutations

CURRENCY_SYMBOLS = ['BTC', 'ETH', 'BNB', 'ADA', 'SOL']
TRAIDING_SYMBOLS = [ ''.join(p) for p in permutations(CURRENCY_SYMBOLS, 2)]




