# %%

import math
import numpy as np
import numpy_financial as nf
import matplotlib.pyplot as pl
import scipy as sp
import scipy.stats as ss
import pandas as pd
import tsemodule5 as tm5

stock2 = tm5.stock("وبصادر")
fig, ax = pl.subplots(figsize= (15, 6))
ax.plot(stock2.index, stock2['<CLOSE>'], 'o-')
ax.grid(True)


# %%
import numpy as np
import matplotlib.pyplot as pl
import pandas as pd
import tsemodule5 as tm5

stock1 = tm5.stock("وبصادر")['<CLOSE>'][::-1]
st1 = stock1.tail(10)
st2 = stock1[:10]

# simple return

# def total_simple_return(stock1):
#      return (stock1 / stock1.shift(1)) - 1

# s = total_simple_return(st2)
# print(s)

# def total_log_return(stock1):
#      return np.log(stock1 / stock1.shift(1))
# total_log_return(st2)

# returns = np.diff(st1/st1[:-1])
# returns

lrs = np.diff(np.log(st1))
lrs

cv = np.std(lrs) / np.mean(lrs)
cv

# %%
