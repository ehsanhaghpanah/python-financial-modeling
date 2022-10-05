# %%
import math
import numpy as np
import numpy_financial as nf
import matplotlib.pyplot as pl
import scipy as sp
import scipy.stats as ss

class CoefficientVariation(object):

     miu: float = 0
     sigma: float = 0

     def __init__(self, m: float, s: float) -> None:
          self.miu = m
          self.sigma = s
          pass

     def value(self) -> float:
          return self.sigma / self.miu

# = CoefficientVariation ======================================


