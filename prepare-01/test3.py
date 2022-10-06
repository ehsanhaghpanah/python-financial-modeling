
# %%

import numpy as np

# Z = np.ones((7, 7))
# Z[2:-2, 1:-1] = 0
# Z

a = np.arange(15)
a

a[a % 5 == 0] *= -1
a

# %%

import numpy as np

x = np.array(['aksha', 'skdj', 'rpoti', '', 'wweyt'], dtype= str)
r = np.char.count(x, 'w')
r
# %%
