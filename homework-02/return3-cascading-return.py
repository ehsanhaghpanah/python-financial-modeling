# %%

import math
import numpy as np
import matplotlib.pyplot as pl
import scipy as sp

def calc_simple_return(p1: float, p2: float, d2: float) -> float:
     return (d2 + (p2 - p1)) / p1

def calc_logarithmic_return(p1: float, p2: float, d2: float) -> float:
     return math.log(d2 + p2) - math.log(p1)

# =============================================================

class CascadingRates(object):

     rates: list = []
     initial_price: float = 0

     def __init__(self, rs: list, ip: float) -> None:
          self.rates = rs
          self.initial_price = ip

     # minus one
     def total_return(self):
          tr = 1
          for rate in self.rates:
               tr = tr * (1 + rate)
          return round((tr - 1), 4)                    # minus one

     #
     def final_price(self):
          return self.initial_price * (1 + self.total_return())

     #
     def net_return(self):
          return self.initial_price * self.total_return()
     
     def average_return(self):
          ar = np.asarray(self.rates)
          return ar.mean()

# = ReturnRates ===============================================

class ReturnRateByPrices(object):

     prices: list = []

     def __init__(self, ps: list) -> None:
          self.prices = ps

     def get_returns_simple(self) -> list:
          rs = []
          for i in range(0, len(self.prices) - 1):
               ri = calc_simple_return(self.prices[i], self.prices[i + 1], 0)
               rs.append(round(ri, 4))
          return rs

     def get_returns_logarithmic(self) -> list:
          rs = []
          for i in range(0, len(self.prices) - 1):
               ri = calc_logarithmic_return(self.prices[i], self.prices[i + 1], 0)
               rs.append(round(ri, 4))
          return rs

     def get_total_return_simple(self):
          return calc_simple_return(self.prices[0], self.prices[-1], 0)

     def get_total_return_logarithmic(self):
          return calc_logarithmic_return(self.prices[0], self.prices[-1], 0)

     def total_return_by_daily_return(self):
          cr = CascadingRates(rr.get_returns_simple(), self.prices[0])
          return cr.total_return()

     def next_period_price_forecast_by_average_price(self):
          ar = np.asarray(self.prices)
          return ar.mean()
     
     def next_period_price_forecast_by_average_return(self):
          ar = np.asarray(self.get_returns_simple())
          av = ar.mean()
          return self.prices[-1] * (1 + av)


# = ReturnRateByPrices ========================================

ls = [6400, 6370, 6090, 5930, 5720, 5990, 6260, 6380, 6660]
rr = ReturnRateByPrices(ls)
print(f'daily simple returns = {rr.get_returns_simple()}')
print(f'daily logarithmic returns = {rr.get_returns_logarithmic()}')
print(f'total simple return = {rr.get_total_return_simple()}')
print(f'total logarithmic return = {rr.get_total_return_logarithmic()}')
print(f'total return by daily returns = {rr.total_return_by_daily_return()}')

# ls = [0.05, 0.1, 0.15]
# cr = CascadingRates(ls, 100)
# print(f'total profit = {cr.total_return()}')
# print(f'final price = {cr.final_price()}')
# print(f'average profit = {cr.average_return()}')

# ls = [6400, 6370, 6090, 5930, 5720, 5990, 6260, 6380, 6660]
# rr = ReturnRateByPrices(ls)
# print(f'daily simple returns = {rr.get_returns_simple()}')
# print(f'total simple return = {rr.get_total_return_simple()}')
# print(f'next period price forecast by average price = {rr.next_period_price_forecast_by_average_price()}')
# print(f'next period price forecast by average return = {rr.next_period_price_forecast_by_average_return()}')

# ls = [16704, 16965, 16360, 16301, 16014, 16475, 15898, 15225, 15089, 15505]
# rr = ReturnRateByPrices(ls)
# print(f'daily simple returns = {rr.get_returns_simple()}')


# ls = [1, 2, 3]
# for i in range(0, len(ls) - 1):
#      print(ls[i])