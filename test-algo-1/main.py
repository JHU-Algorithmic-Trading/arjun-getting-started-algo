# region imports
from AlgorithmImports import *
# endregion

class Testalgo1(QCAlgorithm):

    def initialize(self):
        # Locally Lean installs free sample data, to download more data please visit https://www.quantconnect.com/docs/v2/lean-cli/datasets/downloading-data
        self.set_start_date(2007, 8, 1)
        self.set_end_date(2010, 8, 1)
        self.set_cash(3000)
        
        self.spy = self.add_equity("SPY", Resolution.DAILY)
        self.bnd = self.add_equity("BND", Resolution.DAILY)
        
        self.spy_fast = self.sma("SPY", 10, Resolution.DAILY)
        self.spy_slow = self.sma("SPY", 50, Resolution.DAILY)
        self.bond_fast = self.sma("BND", 10, Resolution.DAILY)
        self.bond_slow = self.sma("BND", 50, Resolution.DAILY)
        
        self.set_benchmark(self.spy.symbol)
        self.set_warm_up(50)
        
        self.profit_target = 0.02
        self.trailing_stop_pct = 0.015
        
        self.entry_prices = {}

    def on_data(self, data: Slice):
        """on_data event is the primary entry point for your algorithm. Each new data point will be pumped in here.
            Arguments:
                data: Slice object keyed by symbol containing the stock data
        """
        if self.is_warming_up:
            return
        
        if self.time.weekday() != 1:
            return
        if "SPY" in data and data["SPY"] is not None:
            if self.spy_fast.current.value > self.spy_slow.current.value:
                if not self.portfolio["SPY"].invested:
                    self.entry_prices["SPY"] = data["SPY"].price
                    self.liquidate("BND")
                    self.set_holdings("SPY", 1)
                else:
                    current_price = data["SPY"].price
                    entry_price = self.entry_prices.get("SPY")
                    if current_price >= entry_price * (1 + self.profit_target):
                        self.liquidate("SPY")
                    elif current_price <= entry_price * (1 - self.trailing_stop_pct):
                        self.liquidate("SPY")

            elif self.spy_fast.current.value < self.spy_slow.current.value:
                self.liquidate("SPY")
        
        if "BND" in data and data["BND"] is not None:
            if self.bond_fast.current.value > self.bond_slow.current.value:
                if not self.portfolio["BND"].invested:
                    self.entry_prices["BND"] = data["BND"].price
                    self.liquidate("SPY")
                    self.set_holdings("BND", 1)
                else:
                    current_price = data["BND"].price
                    entry_price = self.entry_prices.get("BND")
                    if current_price >= entry_price * (1 + self.profit_target):
                        self.liquidate("BND")
                    elif current_price <= entry_price * (1 - self.trailing_stop_pct):
                        self.liquidate("BND")
            
            elif self.bond_fast.current.value < self.bond_slow.current.value:
                self.liquidate("BND")
