# %%

import tsemodule5 as tm5
import pandas as pd
import numpy as np
import matplotlib.pyplot as pl

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

     def mu(self, what: str = 'Close'):  # returns a series of returns
          data: np.array = self.__load__(self.ohlc, self.record_number, what)
          return (data / data.shift(1)) - 1

     def sigma(self, what: str = 'Close') -> float:
          data = self.__load__(self.ohlc, self.record_number, what)
          return data.std()

     def cv(self, what: str = 'Close') -> float:
          data = self.__load__(self.ohlc, self.record_number, what)
          return data.std() / self.mu().mean()

     def draw_complex(self) -> None:
          close  = np.flip(self.ohlc['Close'])
          mu = self.mu()

          fig, axs = pl.subplots(2, 1)
          axs[0].plot(close)
          axs[0].set_xlabel('Date')
          axs[0].set_ylabel('Close')

          axs[1].set_xlabel('Date')
          axs[1].set_ylabel('Daily Return')
          axs[1].bar(mu.index, mu)

          fig.tight_layout(pad= 0.25)
          fig.set_size_inches((10, 5))

          pl.show()
          pass

# = Stock =====================================================

symbol_name = 'فولاد'
record_number = 10  # number of days
stock = Stock(symbol_name, record_number)
mu = stock.mu()
print("daily average")
print(mu)
stock.draw_complex()
print("CV")
print(stock.cv())
