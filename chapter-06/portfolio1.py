import math
import numpy as np
import numpy_financial as nf
import matplotlib.pyplot as pl
import scipy as sp
import scipy.stats as ss

class Asset(object):
     mu: float = 0
     sigma: float = 0
     weight: float = 0

     def __init__(self, m: float, s: float, w: float) -> None:
          self.mu = m
          self.sigma = s
          self.weight = w
          pass

     def reward(self) -> float:
          return self.mu * self.weight
     
     def risk(self) -> float:
          return self.sigma * self.weight

class Portfolio(object):
     assets: list = []

     def __init__(self, al: list) -> None:
          ar = np.asarray([ai.weight for ai in al])
          if (ar.sum() != 1):
               raise Exception("portfolio's assets' weights summation is not one")
          self.assets = al
          pass
     
     # Portfolio Return (Rp)
     # Rate of Return (RoR) of Portfolio
     def reward(self) -> float:
          ls = [li.reward() for li in self.assets]
          return round(sum(ls, 0), 4)
     
     def risk(self) -> float:
          ls = [li.risk() for li in self.assets]
          return round(sum(ls, 0), 4)

# = Portfolio =================================================

# al = []
# al.append(Asset(0.31, 0.01, 0.25))
# al.append(Asset(0.15, 0.01, 0.25))
# al.append(Asset(0.11, 0.01, 0.25))
# al.append(Asset(0.12, 0.01, 0.25))
# pr = Portfolio(al)
# print(f'portfolio return = {pr.reward()}')
# print(f'portfolio risk = {pr.risk()}')

al = []
al.append(Asset(0.174, 0.05, 0.5))
al.append(Asset(0.017, 0.08, 0.5))
pr = Portfolio(al)
print(f'portfolio return = {pr.reward()}')
print(f'portfolio risk = {pr.risk()}')
