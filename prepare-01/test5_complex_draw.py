# %%

import tsemodule5 as tm5
import pandas as pd
import numpy as np
import matplotlib.pyplot as pl

class Stock(object):
     
     symbol_name: str = ""
     record_number: int = 100
     ohlc: pd.DataFrame
     data: np.array

     def __init__(self, sn: str, rn: int = 100) -> None:
          self.symbol_name = sn
          self.record_number = rn

          self.ohlc = tm5.stock(self.symbol_name, standard= True)
          pass
     
     def load(self, what: str = 'Close') -> None:
          self.data = self.ohlc[what]
          self.data = self.data[::-1] # ascending date-time
          self.data = self.data.tail(self.record_number)
          pass

     # data : pandas.core.series.Series
     def get_return_simple(self):  # returns a series of returns
          return (self.data / self.data.shift(1)) - 1

     # data : pandas.core.series.Series
     def get_return_logarithmic(self):  # returns a series of returns
          return np.log(self.data / self.data.shift(1))

     def daily_return(self):
          rls = []
          for i in range(1, len(self.data)):
               ror = ((self.data[i] / self.data[i - 1]) - 1) * 100
               rls.append(round(ror, 2))
          return rls

     def get_std(self):
          return self.data.std()
     
     def draw(self):
          close = self.ohlc['Close']
          high = self.ohlc['High']
          pl.plot(close, color= 'r', label= 'Close')
          pl.plot(high, color= 'b', label= 'High')
          pl.legend()
          pl.show()
          pass

     def foo(self):
          print(f'max = {self.data.max()}')
          print(f'min = {self.data.min()}')
          pass

     def sort(self, what: str = 'Close'):
          temp = self.ohlc[self.ohlc[:, 2].argsort()]
          print(temp)
          pass

     def draw_complex(self) -> None:

          close  = np.flip(self.ohlc['Close'])
          volume = np.flip(self.ohlc['Volume'])

          pl.title = self.symbol_name
          pl.xlabel("time")
          pl.ylabel("price/volume")

          pl.subplot(211)
          pl.plot(close, color= 'b', label= 'Close')
          min_x = list(dict(close))[close.argmin()]
          max_x = list(dict(close))[close.argmax()]
          pl.plot([min_x, max_x], [close.min(), close.max()], color= 'g', label= 'min-max')
          pl.axhline(close.mean(), color= 'red', label= 'mean', linestyle= 'dashed')

          pl.subplot(212)
          pl.bar(x= np.arange(volume.size), height= volume, color= 'orange')

          pl.show()

          pass

# = Stock =====================================================

symbol_name = 'فملي'
record_number = 50

stock = Stock(symbol_name)
stock.load()
# print(f'simple return = {stock.get_return_simple()}')
# print(f'logarithmic return = {stock.get_return_logarithmic()}')
# print(f'daily return = {stock.daily_return()}')
# print(f'standard deviation = {stock.get_std()}')
# stock.draw()

# stock.foo()
stock.draw_complex()

# stock.sort()
