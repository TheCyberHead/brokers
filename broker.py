from cyberhead.brokers.alpaca.alpaca import Alpaca
from pandas import DataFrame


API_KEY = 'PKJE304QMU4UN7PKONAR'
API_SECRET = 'WPrPWhNvxurXjuZdSiXBl/Jc7w9vrH0dKR2BxOSo'
paper_endpoint = 'https://paper-api.alpaca.markets'

brokers = {'alpaca': Alpaca(API_KEY, API_SECRET, paper_endpoint),}

class Broker:

    def __init__(self, name):
        self.name = name
        self.broker = brokers[name]
        self.symbol = 'TSLA'
        self.quantity = 1
        self.prices = DataFrame

        # take the broker informataion only at init
        self.account = self.broker.account
        self.positions = self.broker.positions


    def update(self):
        '''update the information in the broker submodule'''
        self.broker.symbol = self.symbol
        self.broker.quantity =  self.quantity


    def buy(self):
        self.update()
        return self.broker.buy()


    def sell(self):
        self.update()
        return self.broker.sell()
