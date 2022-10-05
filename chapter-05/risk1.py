
import math
import numpy as np
import numpy_financial as nf
import matplotlib.pyplot as pl
import scipy as sp

# data range
def calc_range(ls: list) -> float:
     ar = np.asarray(ls)
     max_v = ar.max()
     min_v = ar.min()
     return max_v - min_v

class SemiVariance(object):

     prices: list = []

     def __init__(self, ps: list) -> None:
          self.prices = ps
          pass
     
     def calc(self) -> float:
          a1 = np.asarray(self.prices)
          av = a1.mean()

          ps = [(pi < av) for pi in self.prices]
          qs = [((pj - av) ** 2) for pj in ps]
          a2 = np.asarray(qs)
          return a2.sum() / (a2.size - 1)
     
# = SemiVariance ============================================== 


