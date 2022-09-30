# %%

import numpy as np
import numpy_financial as fp
import matplotlib.pyplot as pl
import math

z = fp.fv(pv= -20_000_000, rate= 0.2, nper= 5, pmt= 1_000_000, when= 'begin')
z = round(z, 0)
print('{:,}'.format(z))



# %%
