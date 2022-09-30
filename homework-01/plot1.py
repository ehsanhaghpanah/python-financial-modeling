# %%

import numpy as np
import matplotlib.pyplot as pl

def fv(pv: float, r: float, n: int):
     return pv * (1 + r) ** n

def fn(pv: float, r: float, c: str):
     x = np.arange(1, 21, 1)
     y = fv(pv, r, x)
     pl.plot(x, y, color= c)

pv = 1000
ra = [-.06, -.04, -.02, 0, .02, .04, .06]
ca = ['r', 'b', 'c', 'y', 'g', 'm', 'k']
for i in range(7):
     fn(pv, ra[i], ca[i])
pl.show()

# %%
