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

class StockBasket(object):

     stocks: list = []
     duration: int = 10            # number of records

     def __init__(self, symbol_names: list, paths: list, duration = 10) -> None:
          self.symbol_names = symbol_names
          self.duration = duration

          if (len(symbol_names) != len(paths)):
               raise Exception("size not equal")

          for i in range(0, len(symbol_names)):
               self.stocks.append(Stock(symbol_names[i], paths[i], record_number= self.duration))
          pass

     def compare_mu(self):
          for stock in self.stocks:
               print(f'{stock.symbol_name} mu (mean) = {round((stock.mu().mean() * 100), 4)}')
          pass

     def compare_sigma(self):
          for stock in self.stocks:
               print(f'{stock.symbol_name} sigma = {round((stock.sigma() * 100), 4)}')
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

class BetaCalculator(object):

     stock: Stock 
     index: Stock

     def __init__(self, stock: Stock, index: Stock) -> None:
          self.stock = stock
          self.index = index
          pass

     def calc(self, what: str = 'Close'):

          stock_df = pd.DataFrame(self.stock.get_data(what))
          index_df = pd.DataFrame(self.index.get_data(what))

          stock_df["Change"] = stock_df.pct_change(1)
          index_df["Change"] = index_df.pct_change(1)

          ls = stock_df["Change"].dropna().values.reshape(-1, 1)
          li = index_df["Change"].dropna().values.reshape(-1, 1)
          df = pd.DataFrame(np.concatenate((ls, li), axis= 1))
          df.columns = ["Stock", "Index"]
          co = df.cov()                      # cov(stock, index), it is a data frame of (2 x 2)
          cx = co.to_numpy()[1][0]
          vr = self.index.variance()         # var(stock)
          beta = cx / vr                     # beta = cov()
          return beta

# = BetaCalculator ============================================

# symbol_names = ['شستا', 'خساپا', 'شاخص']
# paths = ['data1.csv', 'data2.csv', 'data3.csv']
# sb = StockBasket(symbol_names, paths)

stock1 = Stock('شستا', 'data1.csv')
stock2 = Stock('خساپا', 'data2.csv')
index1 = Stock('شاخص', 'data3.csv')

bc = BetaCalculator(stock1, index1)
print(bc.calc())

