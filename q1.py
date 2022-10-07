# %%

import numpy_financial as nf

cf = [-8000]
for i in range(12):
     cf.append(3000 - 800)
print("cash flows")
print(cf)

npv = nf.npv(0.2, cf)
print(f'npv = {npv}')

n = nf.nper(0.2, 2200, -8000)
print(f'break-even point = {n}')


# %%
