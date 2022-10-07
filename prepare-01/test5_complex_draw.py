# %%

from enum import Enum
import tsemodule5 as tm5
import pandas as pd
import numpy as np
import matplotlib.pyplot as pl

class ReturnKind(Enum):
     SIMPLE = 1,
     LOGARITHMIC = 2

class Stock(object):
     
     symbol_name: str = ""
     record_number: int = 100
     ohlc: pd.DataFrame

     def __init__(self, symbol_name: str, record_number: int = 100) -> None:
          self.symbol_name = symbol_name
          self.record_number = record_number
          self.ohlc = tm5.stock(self.symbol_name, standard= True, value= self.record_number)
          pass

     def __load__(self, ohlc: pd.DataFrame, record_number: int, what: str = 'Close') -> np.ndarray:
          data = ohlc[what]
          data = data[::-1] # ascending date-time
          return data.tail(record_number)

     def mu(self, kind: ReturnKind = ReturnKind.SIMPLE, what: str = 'Close'):  # returns a series of returns
          data: np.array = self.__load__(self.ohlc, self.record_number, what)
          if (kind == ReturnKind.SIMPLE):
               return (data / data.shift(1)) - 1
          else:
               return np.log(data / data.shift(1))

     def sigma(self, what: str = 'Close') -> float:
          data = self.__load__(self.ohlc, self.record_number, what)
          return data.std()

     def variance(self, what: str = 'Close') -> float:
          data = self.__load__(self.ohlc, self.record_number, what)
          return data.var()

     def mean(self, what: str = 'Close') -> float:
          data = self.__load__(self.ohlc, self.record_number, what)
          return data.mean()

     def median(self, what: str = 'Close') -> float:
          data = self.__load__(self.ohlc, self.record_number, what)
          return data.median()

     def max(self, what: str = 'Close') -> float:
          data = self.__load__(self.ohlc, self.record_number, what)
          return data.max()

     def min(self, what: str = 'Close') -> float:
          data = self.__load__(self.ohlc, self.record_number, what)
          return data.min()

     def cv(self, what: str = 'Close') -> float:
          data = self.__load__(self.ohlc, self.record_number, what)
          return data.std() / self.mu().mean()
     
     def draw_special(self):
          close = self.ohlc['Close']
          high = self.ohlc['High']
          pl.plot(close, color= 'r', label= 'Close')
          pl.plot(high, color= 'b', label= 'High')
          pl.legend()
          pl.show()
          pass

     def draw_complex(self) -> None:
          close  = np.flip(self.ohlc['Close'])
          volume = np.flip(self.ohlc['Volume'])

          pl.title = self.symbol_name
          pl.xlabel("time")
          pl.ylabel("price/volume")

          pl.subplot(221)
          pl.plot(close, color= 'b', label= 'Close')
          min_x = list(dict(close))[close.argmin()]
          max_x = list(dict(close))[close.argmax()]
          pl.plot([min_x, max_x], [close.min(), close.max()], color= 'g', label= 'min-max')
          pl.axhline(close.mean(), color= 'red', label= 'mean', linestyle= 'dashed')

          pl.subplot(212)
          pl.bar(x= np.arange(volume.size), height= volume, color= 'orange')

          pl.show()
          pass

     #
     # https://realpython.com/pandas-sort-python/
     def sort(self, what: str = 'Close'):
          return self.ohlc.sort_values(by= what, ascending= True)

     # values between 0 and 1 (Min-Max Scaling)
     def transform1(self, what: str = 'Close'):
          data = self.__load__(self.ohlc, self.record_number, what)

          min_value = data.min()
          max_value = data.max()

          transformed_data = (data - min_value) / (max_value - min_value)
          return transformed_data

     # z-score Standardization (Normalization)
     def transform2(self, what: str = 'Close'):
          data = self.__load__(self.ohlc, self.record_number, what)

          mu = data.mean()
          sigma = data.std()

          transformed_data = (data - mu) / sigma
          return transformed_data

     # number of items greater than mean()
     def foo(self, what: str = 'Close'):
          close = self.__load__(self.ohlc, self.record_number, what)
          a = close[close > close.mean()].size
          print(a)
          b = close[close < close.mean()].size
          print(b)
          pass

# = Stock =====================================================

symbol_name = 'فملي'
record_number = 50
stock = Stock(symbol_name, record_number)
# stock.draw_special()
# stock.draw_complex()
# stock.foo()
# df = stock.sort('Volume')
# df
# df = stock.transform2()
# df

df = stock.mu()[:10]
df
