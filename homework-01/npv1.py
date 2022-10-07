# %%

import numpy as np
import numpy_financial as fp
import matplotlib.pyplot as pl
import math

cash_flows = [-200, 20, 50, 70, 100, 50]
rate = 0.06
npv = fp.npv(rate, cash_flows)
print('npv1 = {:,}'.format(npv))

cash_flows[0] = -250
npv = fp.npv(rate, cash_flows)
print('npv2 = {:,}'.format(npv))


# %%


