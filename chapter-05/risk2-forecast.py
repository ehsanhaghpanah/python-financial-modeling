# %%
import math
import pandas as pd
import numpy as np
import numpy_financial as nf
import matplotlib.pyplot as pl
import scipy as sp
import scipy.stats as ss

class Forecast(object): # =====================================

     items: dict = {}
     props: list = [0.1, 0.2, 0.4, 0.2, 0.1]

     def __init__(self) -> None:
          self.items['A'] = [+0.08, +0.08, +0.08, +0.08, +0.08]
          self.items['B'] = [-0.22, -0.02, +0.20, +0.35, +0.50]
          self.items['C'] = [+0.28, +0.14, +0.00, -0.10, -0.20]
          self.items['D'] = [+0.10, -0.10, +0.07, +0.45, +0.30]
          self.items['E'] = [-0.13, +0.01, +0.15, +0.29, +0.43]
          pass

     def analyze(self, col: str) -> None:
          # ls = [self.items[col][i] * self.props[i] for i in range(0, len(self.props))]
          ls = self.items[col]
          ar = np.asarray(ls)

          print(f'col = {col}, average return (probable) = {round(ar.mean(), 4)}')
          print(f'col = {col}, variance = {round(ar.var(), 4)}')
          print(f'col = {col}, standard deviation = {round(ar.std(), 4)}')
          pass

     def mu(self, col: str) -> float:
          ls = [self.items[col][i] * self.props[i] for i in range(0, len(self.props))]                        # r(i) * p(i)
          ar = np.asarray(ls)
          return round(ar.sum(), 4)                                                                           # sigma(r(i) * p(i))

     def variance(self, col: str) -> float:
          rb = self.mu(col)                                                                      # r-bar (or expected return)
          ls = [(((self.items[col][i] - rb) ** 2) * self.props[i]) for i in range(0, len(self.props))]        # (r(i) - rbar)^2 * p(i)
          ar = np.asarray(ls)
          return round(ar.sum(), 4)                                                                           # sigma((r(i) - rbar)^2 * p(i))
     
     def sigma(self, col: str) -> float:
          return round(math.sqrt(self.variance(col)), 4)

     def analyze_a(self):
          ls: dict = {}
          for nm in self.items:
               ls[nm] = self.mu(nm)
          ls = dict(sorted(ls.items(), key= (lambda item: item[1]), reverse= True))
          for nm in ls:
               print(f'{nm}, expected return = {ls[nm]}')
          pass

     def analyze_b(self):
          ls: dict = {}
          for nm in self.items:
               ls[nm] = self.sigma(nm)
          ls = dict(sorted(ls.items(), key= (lambda item: item[1]), reverse= True))
          for nm in ls:
               print(f'{nm}, standard deviation = {ls[nm]}')
          pass

     def analyze_c(self):
          na = [ni for ni in self.items]
          ma = [self.mu(ni) for ni in na]           # mu
          sa = [self.sigma(ni) for ni in na]        # sigma
          ca = ['r', 'c', 'm', 'y', 'g']

          for i in range(0, len(na)):
               x = np.linspace(ma[i] - (3 * sa[i]), ma[i] + (3 * sa[i]), 100)
               y = ss.norm.pdf(x, ma[i], sa[i])
               pl.plot(x, y, ca[i], label= na[i])
          pl.legend()
          pl.show()
          pass

     def as_data_frame(self) -> pd.DataFrame:
          CV = lambda sigma, miu : round(sigma / miu, 4) if (miu > 0) else math.nan
          dc = {}
          dc['Name'] = [nm for nm in self.items]
          dc['Mu'] = [self.mu(nm) for nm in self.items]
          dc['Sigma'] = [self.sigma(nm) for nm in self.items]
          dc['CV'] = [CV(self.sigma(nm), self.mu(nm)) for nm in self.items]

          df = pd.DataFrame(dc)
          return df

     # mu      : average of samples (x-bar)
     # sigma   : standard deviation
     def draw_normal_distribution_curve(self, col: str, color = 'r') -> None:
          miu = self.mu(col)
          sig = self.sigma(col)

          x = np.linspace(miu - (3 * sig), miu + (3 * sig), 25)
          y = ss.norm.pdf(x, miu, sig)

          pl.plot(x, y, color, label= col, linestyle= 'solid')
          # pl.vlines(np.array([miu]), np.array([0]), np.array([y[np.argwhere(x == miu)]]))
          # pl.vlines(miu, 0, y[np.argwhere(x == miu)])
          pl.vlines(miu, 0, y[np.argwhere(x == miu)], colors= 'b', linestyles= 'dashdot', label= 'mu')
          
          pl.legend()
          pl.show()
          pass

# = Forecast ================================================== 

fo = Forecast()
fo.analyze_b()
fo.analyze_c()
fo.draw_normal_distribution_curve('B')
df = fo.as_data_frame()
df

# %%
