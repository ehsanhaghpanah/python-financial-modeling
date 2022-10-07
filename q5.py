# %%

import numpy as np
import matplotlib.pyplot as pl

def f(x):
     return x ** 2 + 9 * x + 14

x = np.linspace(-10, 10, 1000)
y = f(x)

# calculating minimum (x, y)
min_x = x[y.argmin()]
min_y = f(x[y.argmin()])

pl.plot(x, y, color = 'b')
pl.plot(min_x, min_y, 'ro')
pl.show()


# %%
