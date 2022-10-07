
# %%

import numpy_financial as nf

pv = [-500]
pmt = [50, 31, 3, 11]
cf = pv + pmt

irr = nf.irr(cf)
print(round(irr, 4))

# %%

import numpy_financial as nf

n = nf.nper(0.1/12, -100, 10_000)
print(n)


# %%

import numpy_financial as nf

cf = [-500_000, 160_000, 160_000, 160_000, 160_000, 50_000]
irr = nf.irr(cf)
print(type(irr))
npv = nf.npv(irr, cf)
print(f'{npv:.7f}')
x = nf.npv(0.13, [-500_000, 160_000, 160_000, 160_000, 160_000, 50_000])
print(x)


# %%

import numpy_financial as nf

# cf = [-10, -8, 50]
# x = nf.pv(0.2, 2, cf)
# print(x)

x = nf.npv(.2, [-10, -8, 50])
x

# %%

