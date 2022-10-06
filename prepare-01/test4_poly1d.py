# %%

import numpy as np
import matplotlib.pyplot as pl

yf = np.poly1d([1, 5, 0, 10])
y2 = np.polyder(yf, m = 1)
y3 = np.polyder(y2, m = 1)
# print(yf)
# print(y2)
# print(y3)

x = np.linspace(-5, 2, 100)
pl.plot(x, yf(x), color='r', label= 'yf')
pl.plot(x, y2(x), color='b', label= 'y2')
pl.plot(x, y3(x), color='g', label= 'y3')
pl.xlabel('x', loc= 'center')
pl.ylabel('y', loc= 'center')
pl.legend()
pl.show()

# %%
import numpy as np
import matplotlib.pyplot as pl

y1 = np.poly1d([0, 0, 3, 4])
y2 = np.polyint(y1, m= 1)

x = np.linspace(-5, 5, 100)
pl.plot(x, y1(x), color='r', label= 'y1')
pl.plot(x, y2(x), color='b', label= 'y2')
pl.xlabel('x', loc= 'center')
pl.ylabel('y', loc= 'center')
pl.legend()
pl.show()

