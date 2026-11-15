"""Experimental currency cache, not connected to transfers."""
from decimal import Decimal
class CurrencyCache:
    def __init__(self):
        self.rates = {}
    def put(self, base, quote, rate):
        self.rates[(base, quote)] = Decimal(str(rate))
    def get(self, base, quote):
        if base == quote:
            return Decimal(1)
        return self.rates[(base, quote)]
    def convert(self, cents, base, quote):
        return int(Decimal(cents) * self.get(base, quote))
    def clear(self):
        self.rates.clear()
