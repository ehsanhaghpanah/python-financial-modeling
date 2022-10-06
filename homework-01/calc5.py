# %%

import numpy as np
import numpy_financial as fp
import matplotlib.pyplot as pl
import math

# z = fp.fv(pv= -20_000_000, rate= 0.2, nper= 5, pmt= 1_000_000, when= 'begin')
# z = round(z, 0)
# print('{:,}'.format(z))

# z = fp.fv(pv= 0, rate= 0.12, nper= 9, pmt= -150_000, when= 'end')
# z = round(z, 0)
# print('{:,}'.format(z))

# m = 7_500_000 * 12
# z = fp.fv(pv= 0, rate= 0.16, nper= 4, pmt= -m, when= 'end')
# z = round(z, 0)
# print('{:,}'.format(z))

# r = 0.16 / 12
# n = 4 * 12
# z = fp.fv(pv= 0, rate= r, nper= n, pmt= -7_500_000, when= 'end')
# z = round(z, 0)
# print('{:,}'.format(z))

# z = fp.fv(pv= 0, rate= 0.08, nper= 5, pmt= -10_000, when= 'end')
# z = round(z, 0)
# print('{:,}'.format(z))

z1 = round(fp.fv(pv= -15_000, rate= 0.05, nper= 10, pmt= 0), 0)
z2 = round(fp.fv(pv= -15_000, rate= 0.10, nper= 12, pmt= 0), 0)
z3 = round(fp.fv(pv= -15_000, rate= 0.15, nper= 18, pmt= 0), 0)
print('{:,}'.format(z1))
print('{:,}'.format(z2))
print('{:,}'.format(z3))

# z1 = round(fp.fv(pv= 0, rate= 0.05, nper= 10, pmt= -15_000), 0)
# z2 = round(fp.fv(pv= 0, rate= 0.10, nper= 12, pmt= -15_000), 0)
# z3 = round(fp.fv(pv= 0, rate= 0.15, nper= 18, pmt= -15_000), 0)
# print('{:,}'.format(z1))
# print('{:,}'.format(z2))
# print('{:,}'.format(z3))

# %%
