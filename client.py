import asyncio
from binance.spot import Spot
from api_config import (KEY, SECRET, TIMEOUT)

from requests.exceptions import ( ConnectionError, HTTPError )
from binance.error import ClientError

from decimal import Decimal

spot = Spot(key=KEY, secret=SECRET, timeout=TIMEOUT)

class Account:
    balance_list = []

    async def update_account(self):
        while True:
            try:
                self.__transform(spot.account())
                return
            except Exception as exception:
                if(isinstance(exception, ConnectionError)):
                    print("---> ConnectionError")
                elif(isinstance(exception, HTTPError)):
                    print("---> HTTPError")
                elif(isinstance(exception, ClientError)):
                    print("---> ClientError")
                else:
                    print(f"---> Oops!!! \n {type(exception)}")
                print("trying Account.update_account again in 5 seconds...")
                await asyncio.sleep(5)
                self.update_account()

    def get_asset_symbol_list(self):
        return [b.asset for b in self.balance_list]

    def __transform(self, account):
        self.balance_list = [b for b in [ Balance(e) for e in account['balances'] ] if b.free > 0 or b.locked > 0 ]

class Balance:
    asset = ""
    free = Decimal(0)
    locked = Decimal(0)

    def __init__(self, balance):
        self.asset = balance['asset']
        self.free = Decimal(balance['free'])
        self.locked = Decimal(balance['locked'])

account = Account()

