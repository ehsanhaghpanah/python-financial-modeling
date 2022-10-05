# %%
import math
import numpy as np
import numpy_financial as nf
import matplotlib.figure as fg
import matplotlib.pyplot as pl
import scipy as sp
import scipy.stats as ss

# mu      : average of samples (x-bar)
# sigma   : standard deviation
def draw_normal_distribution_curve(miu: float, sig: float, color = 'r') -> fg.Figure:

     x = np.linspace(miu - (3 * sig), miu + (3 * sig), 25)
     y = ss.norm.pdf(x, miu, sig)

     pl.plot(x, y, color, label= '', linestyle= 'solid')
     pl.vlines(miu, 0, y[np.argwhere(x == miu)], colors= 'b', linestyles= 'dashdot', label= 'mu')
     
     pl.legend()
     pl.show()
     return pl.figure()

# = draw_normal_distribution_curve ============================

def draw_multiple(data: list) -> None:

     for i in range(0, len(data)):
          miu = data[i][0]
          sig = data[i][1]
          cor = data[i][2]
          x = np.linspace(miu - (3 * sig), miu + (3 * sig), 100)
          y = ss.norm.pdf(x, miu, sig)
          pl.plot(x, y, cor, label= '', linestyle= 'solid')
     pl.legend()
     pl.show()
     pass

# = draw_multiple =============================================

ls = [(+0, 0.7, 'r'), (+0, 1.0, 'b'), (+1, 1.5, 'g'), (-2, 0.5, 'm')]
draw_multiple(ls)

# %%
