# %%

import numpy as np
import pandas as pa

ls = [1, 2, 3, 4, 5]
sa = pa.Series(ls)
print(sa)
sb = sa.shift(-1)
print(sb)

# %%

import pandas as pa

dc = {}
l1 = [18, 19, 16, 12, 13, 11, 15, 14, 17]
l2 = [24, 25, 26, 21, 22, 27, 28, 23, 29]
dc['l1'] = l1
dc['l2'] = l2

df = pa.DataFrame(dc)
# d2 = df.sort_values(by= 'l1', ascending= True)
# d2

d2 = df.sort
d2

# d2 = df[:,2].argsort()
# d2
