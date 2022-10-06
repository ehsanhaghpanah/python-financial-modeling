
import math
import numpy as np
import matplotlib.pyplot as pl
import scipy as sp

class GeometricMean(object):
     
     values: list = []

     def __init__(self, vs: list) -> None:
          self.values = vs
          pass

     #
     # Cumulative Simple Return Rates
     # R(total) = [(1 + R(1)) * (1 + R(2)) * ... * (1 + R(n))] - 1
     # total return MINUS 1 (one)
     def total_mean(self):
          tr = 1
          for rate in self.values:
               tr = tr * (1 + rate)
          return round((tr - 1), 4)

     def total_mean_nroot(self):
          ar = np.asarray(self.values)
          return round(ar.prod() ** (1 / len(self.values)), 4)

     def get_geometric_average(self):
          ar = np.asarray(self.values)
          ar = ar + 1
          return round((ar.prod() ** (1 / ar.size)) - 1, 4)

# = GeometricMean =============================================

class ArithmeticMean(object):
     
     values: list = []

     def __init__(self, vs: list) -> None:
          self.values = vs
          pass

     def total_mean(self):
          ar = np.asarray(self.values)
          return round(ar.mean(), 4)

# = ArithmeticMean ============================================

# ls = [4, 2, 6, 27]
# gm = GeometricMean(ls)
# print(f'total geometric mean = {gm.total_mean_nroot()}')

# ls = [0.8, -0.8]
# gm = GeometricMean(ls)
# print(f'total geometric mean = {gm.total_mean()}')
# print(f'total geometric average = {gm.get_geometric_average()}')

# ls = [0.14, 0.06, -0.05, 0.2]
# gm = GeometricMean(ls)
# print(f'total geometric mean = {gm.total_mean()}')
# print(f'total geometric average = {gm.get_geometric_average()}')

ls = [0.05, 0.1, 0.15]
gm = GeometricMean(ls)
print(f'total geometric mean = {gm.total_mean()}')
print(f'total geometric average = {gm.get_geometric_average()}')