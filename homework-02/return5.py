
class HarmonicMean(object):

     values: list = []

     def __init__(self, vs: list) -> None:
          self.values = vs
          pass

     def get_average(self):
          rs = 0
          for vi in self.values:
               rs = rs + (1 / vi)
          return (len(self.values) / rs)

# = HarmonicMean ==============================================

# ls = [17, 18, 19, 20]
# hm = HarmonicMean(ls)
# print(f'harmonic average = {hm.get_average()}')

ls = [60, 30]
hm = HarmonicMean(ls)
print(f'harmonic average = {hm.get_average()}')
