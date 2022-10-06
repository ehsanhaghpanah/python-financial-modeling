# %%

import tsemodule5 as tm5
import pandas as pd
import numpy as np

# data : pandas.core.series.Series
def get_return_simple(data):  # returns a series of returns
     return (data / data.shift(1)) - 1

# data : pandas.core.series.Series
def get_return_logarithmic(data):  # returns a series of returns
     return np.log(data / data.shift(1))

def daily_return(data):
     rls = []
     for i in range(1, len(data)):
          ror = ((data[i] / data[i - 1]) - 1) * 100
          rls.append(round(ror, 2))
     return rls

symbol_name = 'فملي'
record_number = 10

ohlc = tm5.stock(symbol_name, standard= True)
close = ohlc['Close']
close = close[::-1] # ascending date-time
close = close.tail(record_number)

return_s = get_return_simple(close)
return_l = get_return_logarithmic(close)

return_d = daily_return(close)
return_d


# %%
