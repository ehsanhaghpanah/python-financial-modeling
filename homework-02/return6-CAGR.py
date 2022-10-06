
# Compound Annual Growth Rate (CAGR)
class CAGR(object):

     prices: list = []

     def __init__(self, ps: list) -> None:
          self.prices = ps
          pass

     def getCAGR(self) -> float:
          return ((self.prices[-1] / self.prices[0]) ** (1 / len(self.prices))) - 1

# = CAGR ======================================================

ls = [900, 1100, 1150, 1300]
cagr = CAGR(ls)
print(f'CAGR = {cagr.getCAGR()}')