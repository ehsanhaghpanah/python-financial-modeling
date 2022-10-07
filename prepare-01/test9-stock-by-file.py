
# %%

from turtle import color
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
     ohlc: pd.DataFrame

     def __init__(self, symbol_name: str, path: str, record_number: int = 100) -> None:
          self.symbol_name = symbol_name
          self.record_number = record_number

          try:          
               data = pd.read_csv(path, index_col= "<DTYYYYMMDD>", parse_dates= True)
               data = data.rename(columns={"<OPEN>": "Open", "<CLOSE>": "Close", "<HIGH>":"High", "<LOW>":"Low", "<VOL>":"Volume"})
               data.index.rename('Date', inplace= True)
               data.drop(["<TICKER>", "<FIRST>", "<VALUE>", "<OPENINT>", "<PER>", "<LAST>"], axis= 1, inplace= True)
               self.ohlc = data.head(self.record_number)
          except Exception as e:
               print(f'Error = {e.message}, args = {e.args}')
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

     # risk-free 
     def sharpe(self, rf: float, what: str = 'Close') -> float:
          data = self.__load__(self.ohlc, self.record_number, what)
          return (self.mu(what).mean() - rf) / data.std()

     def semi_variance(self, what: str = 'Close') -> float:
          data = self.__load__(self.ohlc, self.record_number, what)
          a1 = np.asarray(data)
          av = a1.mean()
          ps = [(pi < av) for pi in data]
          qs = [((pj - av) ** 2) for pj in ps]
          a2 = np.asarray(qs)
          return a2.sum() / (a2.size - 1)

     def sortino(self, rf: float, what: str = 'Close') -> float:
          sv = self.semi_variance(what)
          mu = self.mu(what).mean()
          return (mu - rf) / sv ** 0.5

     def draw(self, what: str = 'Close') -> None:
          data = self.__load__(self.ohlc, self.record_number, what)
          pl.title = self.symbol_name
          pl.xlabel("time")
          pl.ylabel(what)
          pl.plot(data, color= 'b', label= what)
          min_x = list(dict(data))[data.argmin()]
          max_x = list(dict(data))[data.argmax()]
          pl.plot([min_x, max_x], [data.min(), data.max()], color= 'g', label= 'min-max')
          pl.axhline(data.mean(), color= 'red', label= 'mean', linestyle= 'dashed')
          pl.show()
          pass

     def draw_sigma_band(self, what: str = 'Close') -> None:
          data = self.__load__(self.ohlc, self.record_number, what)
          band_upper = data + data.std()
          band_lower = data - data.std()
          pl.title = self.symbol_name
          pl.xlabel("time")
          pl.ylabel(what)
          pl.plot(data, color= 'b', label= what)
          min_x = list(dict(data))[data.argmin()]
          max_x = list(dict(data))[data.argmax()]
          pl.plot(min_x, data.min(), 'ro')
          pl.plot(max_x, data.max(), 'ro')
          pl.plot(band_upper, color= 'y', label= what, linestyle= 'dashdot')
          pl.plot(band_lower, color= 'y', label= what, linestyle= 'dashdot')
          pl.show()
          pass

     def draw_special(self):
          close = self.ohlc['Close']
          high = self.ohlc['High']
          pl.plot(close, color= 'r', label= 'Close')
          pl.plot(high, color= 'b', label= 'High')
          pl.legend()
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

     # adding a column to dataset
     def get_data(self, what: str = 'Close'):
          data = self.__load__(self.ohlc, self.record_number, what)
          return data

# = Stock =====================================================

stock1 = Stock('شستا', 'data.csv')

def foo():
     close = stock1.get_data()
     vol = stock1.get_data('Volume')

     x_min, y_min = close.loc[close == close.min()].index, close[close == close.min()]
     x_max, y_max = close.loc[close == close.max()].index, close[close == close.max()]

     h_mean = close.mean()

     o_mean = np.array([1 for c in close if c >= h_mean]).sum()
     b_mean = np.array([1 for c in close if c < h_mean]).sum()

     print(f'over mean = {o_mean}')
     print(f'below mean = {b_mean}')

     fig, axs = pl.subplots(2, 1)        # rows, cols
     axs[0].plot(close)
     axs[0].set_xlabel('Date')
     axs[0].set_ylabel('Close')
     axs[0].axhline(h_mean, color= 'r')
     axs[0].plot(x_min, y_min, 'o', markersize= 5, color= 'm', label= 'BUY')
     axs[0].plot(x_max, y_max, 'o', markersize= 5, color= 'm', label= 'SEL')
     axs[0].plot([x_min, x_max], [y_min, y_max], color= 'y')
     axs[0].grid(True)

     axs[1].set_xlabel('Date')
     axs[1].set_ylabel('Volume')
     axs[1].bar(vol.index, vol)

     fig.tight_layout(pad= 0.25)
     fig.set_size_inches((7.5, 7.5))

print(stock1.sharpe(.1))
print(stock1.semi_variance())
