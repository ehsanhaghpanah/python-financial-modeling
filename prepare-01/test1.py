# %%

import math
import numpy as np
import numpy_financial as nf
import matplotlib.pyplot as pl
import scipy as sp
import scipy.stats as ss
import tsemodule5 as tm5

path = "data.csv"
data = np.genfromtxt(path, delimiter= ',', names= True)

close = data["CLOSE"]
# print(close.shape)
# print(close.size)
# print(f'max = {close.max()}')
# print(f'min = {close.min()}')
# print(f'argmax = {close.argmax()}')
# print(f'argmin = {close.argmin()}')
# print(f'mean = {close.mean()}')
# print(f'std = {close.std()}')
# n1 = close[close > close.mean()].size
# print(n1)
# np.unique(close > close.mean(), return_counts= True)
# (array([False,  True]), array([822, 556], dtype=int64))


# %%

import math
import numpy as np
import numpy_financial as nf
import matplotlib.pyplot as pl
import scipy as sp
import scipy.stats as ss
import tsemodule5 as tm5
import pandas as pd

path = "data.csv"
df = pd.read_csv(path, index_col= "<DTYYYYMMDD>", parse_dates= True)
data = df['<CLOSE>']
vol = df['<VOL>']

x_min, y_min = data.loc[data == data.min()].index, data[data == data.min()]
x_max, y_max = data.loc[data == data.max()].index, data[data == data.max()]

y_mean = data.mean()

over_mean = np.array([1 for i in data if i < y_mean]).sum()
below_mean = np.array([1 for i in data if i < y_mean]).sum()

fig, axs = pl.subplots(2, 1)
axs[0].plot(data)
axs[1].set_xlabel('Date')
axs[0].set_ylabel('Close')
axs[1].set_ylabel('Volume')
axs[0].axhline(y_mean, color= 'blue')
axs[0].plot(x_min, y_min, '^', markersize= 7, color= 'k', label= 'buy')
axs[0].plot(x_max, y_max, '>', markersize= 7, color= 'k', label= 'sell')

x = [x_min, x_max]
y = [y_min, y_max]

axs[0].plot(x, y, 'r')
axs[1].bar(vol.index, vol)


# %%

