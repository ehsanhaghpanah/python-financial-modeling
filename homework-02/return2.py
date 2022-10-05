

# 
class ReturnRates(object):

     rates: list = []
     initial_price: float = 0

     def __init__(self, rs: list, ip: float) -> None:
          self.rates = rs
          self.initial_price = ip

     #
     def total_return(self):
          tr = 1
          for rate in self.rates:
               tr = tr * (1 + rate)
          return (tr - 1)

     #
     def final_price(self):
          return self.initial_price * (1 + self.total_return())

     #
     def net_return(self):
          return self.initial_price * self.total_return()

# ReturnRates =================================================

# ls = [.12, .1, -0.05, .15]
# rr = ReturnRates(ls, 100)
# print(f'total return rate = {rr.total_return()}')

# ls = [.1, .12, -0.06]
# rr = ReturnRates(ls, 200)
# print(f'total return rate = {rr.total_return()}')
# print(f'total return rate = {rr.final_price()}')
# print(f'total return rate = {rr.net_return()}')

ls = [.1, .12, -0.06]
rr = ReturnRates(ls, 200)
print(f'total return rate = {rr.total_return()}')
print(f'total return rate = {rr.final_price()}')
print(f'total return rate = {rr.net_return()}')
