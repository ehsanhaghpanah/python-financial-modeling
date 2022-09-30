# %%

import numpy as np
import numpy_financial as fp
import matplotlib.pyplot as pl
import math

def fv_simple(pv: float, r: float, n: int):
     return pv * (1 + r) ** n

def pv_simple(fv: float, r: float, n: int):
     return fv / (1 + r) ** n

#
# payment at the end of each period
def fv_ed_pmt(pmt: float, r: float, n: int):
     return pmt * ((((1 + r) ** n) - 1)/r)

#
# payment at the beginning of each period = payment in advanced
def fv_ad_pmt(pmt: float, r: float, n: int):
     return pmt * (1 + r) * ((((1 + r) ** n) - 1)/r)

#
# sigma fv(s) : payment at the end of each period
def fv_ed(pv: float, pmt: float, r: float, n: int):
     return fv_simple(pv, r, n) + fv_ed_pmt(pmt, r, n)

#
# sigma fv(s) : payment in advanced
def fv_ad(pv: float, pmt: float, r: float, n: int):
     return fv_simple(pv, r, n) + fv_ad_pmt(pmt, r, n)

#
# payment at the end of each period
# discouting a series of payment at the end of each period
def pv_ed_pmt(pmt: float, r: float, n: int):
     return pmt * ((1 - (1 / ((1 + r) ** n))) / r)

# pv = 5_000_000
# r = 0.2
# n = 3
# pmt = 1_000_000
# z = round(fv_ed(pv, pmt, r, n), 0)
# print('{:,}'.format(z))

# pv = 5_000_000
# r = 0.2
# n = 3
# pmt = 1_000_000
# z = round(fv_ad(pv, pmt, r, n), 0)
# print('{:,}'.format(z))

pv = 1_328_000
r = 0.1
n = 5
pmt = 500_000
z = round(fv_ad(pv, pmt, r, n), 0)
print('{:,}'.format(z))


# %%
