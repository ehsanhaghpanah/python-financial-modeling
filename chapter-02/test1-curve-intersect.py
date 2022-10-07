#
# (C) Ehsan Haghpanah, 2022.
#

# %%

import numpy as np
import matplotlib.pyplot as pl

#
# any given function(s) of one single variable
def f1(x):
	return x ** 2 + 3
def f2(x):
	return 3 * (x ** 2) + (5 * x) + 2

#
# defining x range
x = np.linspace(-3, 3, 1000)

y = f1(x)
z = f2(x)

#
# calculating a series of signs and differences to check where cross over happens
s = np.sign(y - z)
d = np.diff(s)			# diff[i] = s[i+1] - s[i]

#
# extracting cross over indices on x axis
# returns non-zero indices
i = np.argwhere(d)

#
# visualization
pl.plot(x, y, label = "y = x ** 2 + 3")
pl.plot(x, z, label = "z = 3 * (x ** 2) + (5 * x) + 2")
pl.plot(x[i], y[i], 'ro')
for j in i:
	pl.text(x[j.item(0)], y[j.item(0)], f"({round(x[j.item(0)], 3)}, {round(y[j.item(0)], 3)})", horizontalalignment= 'center')

pl.title("two functions cross over(s)")
pl.xlabel("x")
pl.ylabel("y, z")
pl.legend()
pl.show()
# %%
