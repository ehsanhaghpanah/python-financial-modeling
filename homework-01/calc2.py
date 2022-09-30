# %%

import numpy as np
import matplotlib.pyplot as pl
import math

def fv(pv: float, r: float, n: int, m: int):
     return pv * (1 + (r / m)) ** (n * m)

def pv(fv: float, r: float, n: int, m: int):
     return fv / (1 + (r / m)) ** (n * m)

def ir(pv: float, fv: float, n: int, m: int):
     return (((fv / pv) ** (1 / (n * m))) - 1) * m

def nt(pv: float, fv: float, r: float, m: int):
     return math.log(fv / pv) / (math.log(1 + (r / m)) * m)

# pv = 5_000_000
# r = 0.2
# n = 3
# m = 4
# z = round(fv(pv, r, n, m), 2)
# print('{:,}'.format(z))

fv = 35_917_126
r = 0.2
n = 3
m = 4
z = round(pv(fv, r, n, m), 0)
print('{:,}'.format(z))

# %%
