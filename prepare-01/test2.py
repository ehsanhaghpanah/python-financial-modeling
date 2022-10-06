# %%

import tsemodule5 as tm5
import pandas as pd
import numpy as np

symbol_names = ['فملي', 'فولاد', 'شستا']
record_number = 10

# data : pandas.core.series.Series
def get_return_simple(data):  # returns a series of returns
     return (data / data.shift(1)) - 1

# data : pandas.core.series.Series
def get_return_logarithmic(data):  # returns a series of returns
     return np.log(data / data.shift(1))

df = pd.DataFrame()

for symbol_name in symbol_names:
     ohlc = tm5.stock(symbol_name, standard= True)
     close = ohlc['Close']         # data set (close)
     close = close[::-1]           # ascending date-time
     df[symbol_name] = close.tail(record_number)

return_s = get_return_simple(df)
return_s


# %%
