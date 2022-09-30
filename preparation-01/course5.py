# %%

import numpy as np
import matplotlib.pyplot as pl

def fv(pv: float, r: float, n: int):
     return pv * (1 + r) ** n

pv = 5_000_000
r = 0.2



# %%
