# %%

import tsemodule5 as tm5
import pandas as pd
import numpy as np
import matplotlib.pyplot as pl
from enum import Enum

class ReturnKind(Enum):
     SIMPLE = 1,
     LOGARITHMIC = 2

class Stock(object):
     
     symbol_name: str = ""
     record_number: int = 100
     prices: list = []

     def __init__(self, symbol_name: str, prices: list) -> None:
          self.symbol_name = symbol_name
          self.prices = prices
          pass

     def mu(self, kind: ReturnKind = ReturnKind.SIMPLE):  # returns a series of returns
          data = pd.Series(self.prices)
          if (kind == ReturnKind.SIMPLE):
               return (data / data.shift(1)) - 1
          else:
               return np.log(data / data.shift(1))

     def sigma(self) -> float:
          data = pd.Series(self.prices)
          return data.std()

     def variance(self) -> float:
          data = pd.Series(self.prices)
          return data.var()

     def mean(self) -> float:
          data = pd.Series(self.prices)
          return data.mean()

     def median(self) -> float:
          data = pd.Series(self.prices)
          return data.median()

     def max(self) -> float:
          data = pd.Series(self.prices)
          return data.max()

     def min(self) -> float:
          data = pd.Series(self.prices)
          return data.min()

     def cv(self) -> float:
          data = pd.Series(self.prices)
          return data.std() / self.mu().mean()

     def draw(self) -> None:
          data = pd.Series(self.prices)
          pl.title = self.symbol_name
          pl.xlabel("time")
          pl.ylabel("price")
          pl.plot(data, color= 'b', label= 'price')
          min_x = list(dict(data))[data.argmin()]
          max_x = list(dict(data))[data.argmax()]
          pl.plot([min_x, max_x], [data.min(), data.max()], color= 'g', label= 'min-max')
          pl.axhline(data.mean(), color= 'red', label= 'mean', linestyle= 'dashed')
          pl.show()
          pass

     def draw_sigma_band(self) -> None:
          data = pd.Series(self.prices)
          band_upper = data + data.std()
          band_lower = data - data.std()
          pl.title = self.symbol_name
          pl.xlabel("time")
          pl.ylabel('price')
          pl.plot(data, color= 'b', label= 'price')
          min_x = list(dict(data))[data.argmin()]
          max_x = list(dict(data))[data.argmax()]
          pl.plot(min_x, data.min(), 'ro')
          pl.plot(max_x, data.max(), 'ro')
          pl.plot(band_upper, color= 'y', label= 'price', linestyle= 'dashdot')
          pl.plot(band_lower, color= 'y', label= 'price', linestyle= 'dashdot')
          pl.show()
          pass

     def draw_mu(self):
          data = self.mu()
          pl.title = self.symbol_name
          pl.xlabel("time")
          pl.ylabel('mu')
          pl.plot(data, color= 'b', label= 'mu')
          pl.axhline(data.mean(), color= 'red', label= 'mean', linestyle= 'dashed')
          pl.show()
          pass

# = Stock =====================================================

class StockBasket(object):

     stocks: list = []

     def __init__(self, stocks: list) -> None:
          self.stocks = stocks
          pass

     def as_data_frame1(self) -> pd.DataFrame:
          dc = {}
          dc['Symbol Name'] = [stock.symbol_name for stock in self.stocks]
          dc['Mu'] = [round(stock.mu().mean(), 4) * 100 for stock in self.stocks]
          dc['Sigma'] = [round(stock.sigma(), 2) for stock in self.stocks]
          dc['max'] = [round(stock.max(), 4) for stock in self.stocks]
          dc['min'] = [round(stock.min(), 4) for stock in self.stocks]
          dc['variance'] = [round(stock.variance(), 4) for stock in self.stocks]
          dc['mean price'] = [round(stock.mean(), 4) for stock in self.stocks]

          df = pd.DataFrame(dc)
          return df

     def as_data_frame2(self) -> pd.DataFrame:

          dc = {}
          dc['Symbol Name'] = [stock.symbol_name for stock in self.stocks]
          dc['Mu'] = [round(stock.mu().mean(), 4) * 100 for stock in self.stocks]
          dc['CV'] = [round(stock.cv(), 0) for stock in self.stocks]
          dc['sigma'] = [round(stock.variance(), 0) for stock in self.stocks]

          df = pd.DataFrame(dc)
          return df

# = StockBasket ===============================================

ls = []
ls.append(Stock('stock1', [6400, 6370, 6090, 5930, 5720, 5990, 6260, 6380, 6660]))
ls.append(Stock('stock2', [5410, 5886, 5959, 5899, 5999, 6245, 6440, 6670, 6881]))
ls.append(Stock('index1', [1229837, 1260723, 1301326, 1306621, 1285892, 1310756, 1350233, 1374483, 1355351]))
sb = StockBasket(ls)
df = sb.as_data_frame2()
df

