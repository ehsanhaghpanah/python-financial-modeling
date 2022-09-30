# %%

import numpy as np
import matplotlib.pyplot as pl
import math

def simple_intreset_rate(pv: float, r: float, n: int):
     return pv * (1 + (n * r))

def fv(pv: float, r: float, n: int):
     return pv * (1 + r) ** n

def pv(fv: float, r: float, n: int):
     return fv / (1 + r) ** n

def ir(pv: float, fv: float, n: int):
     return ((fv / pv) ** (1 / n)) - 1

def nt(pv: float, fv: float, r: float):
     return math.log(fv / pv) / math.log(1 + r)

# pv = 5_000_000
# r = 0.2
# n = 3
# z = round(fv(pv, r, n), 2)
# print('{:,}'.format(z))

# pv = 1000
# fv = 2000
# r = 0.1
# z = round(nt(pv, fv, r), 2)
# print('{:,}'.format(z))

fv = 60_480_000
r = 0.2
z = round(pv(fv, r, 3), 2)
print('{:,}'.format(z))


# %%
