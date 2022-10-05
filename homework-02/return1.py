import math

class SimpleReturnRate(object):

     def __init__(self, p1: float, p2: float, d2: float) -> None:
          self.p1 = p1
          self.p2 = p2
          self.d2 = d2

     p1: float = 0.0
     p2: float = 0.0
     d2: float = 0.0

     def get_return(self):
          return (self.d2 + (self.p2 - self.p1)) / self.p1

# = SimpleReturnRate ==========================================

class LogarithmicReturnRate(object):

     def __init__(self, p1: float, p2: float, d2: float) -> None:
          self.p1 = p1
          self.p2 = p2
          self.d2 = d2

     p1: float = 0.0
     p2: float = 0.0
     d2: float = 0.0

     def get_return(self):
          return math.log(self.d2 + self.p2) - math.log(self.p1)

     # def calc1(self):
     #      return math.log((self.d2 + (self.p2 - self.p1)) / self.p1)
     # def calc2(self):
     #      return math.log((self.d2 + self.p2) / self.p1)

# = LogarithmicReturnRate =====================================

# srr = SimpleReturnRate(100, 114, 0)
# lrr = LogarithmicReturnRate(100, 114, 0)

# print(f'simple return rate = {srr.calc()}')
# print(f'logarithic return rate = {lrr.calc3()}')

srr = SimpleReturnRate(10, 9.5, 1)
print(f'simple return rate = {srr.get_return()}')
