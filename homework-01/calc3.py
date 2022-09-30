# %%

import numpy as np
import matplotlib.pyplot as pl
import math

def fv(pv: float, r: float, n: int):
     return pv * math.exp(r * n)

def pv(fv: float, r: float, n: int):
     return fv / math.exp(r * n)

def ir(pv: float, fv: float, n: int):
     return math.log(fv / pv) / n

def nt(pv: float, fv: float, r: float):
     return math.log(fv / pv) / r

# pv = 5_000_000
# r = 0.2
# n = 3
# z = round(fv(pv, r, n), 2)
# print('{:,}'.format(z))

fv = 9_110_594
r = 0.2
n = 3
z = round(pv(fv, r, n), 2)
print('{:,}'.format(z))


# %%
