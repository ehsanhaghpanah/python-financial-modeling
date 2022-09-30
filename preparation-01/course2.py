
# %%

import numpy as np

g = np.array([1, 2, 3, 4, 5])
w = np.array([9, 1, 1, 1, 1])

v = np.average(g, weights= w)
print(v)

# %%

import numpy as np

p = np.array([100, 200, 300, 400])
g = p / p[0]

print(g)
print(g[-1])

# %%

import numpy as np

a = np.array([1, 2, 3, 4, 5, 6])
b = a.reshape(2, 3)
print(b)
c = b.flatten()
print(c)

d = b.ravel('K')
print(d)

# %%

import numpy as np

a = np.array([1, 2, 7, 4, 5, 6])
b = np.flip(a)
print(b)

c = np.sort(a)
print(c)

# %%

import numpy as np

a = np.array([[1, 2, 7], [4, 5, 2], [9, 8, 7]])
print(a)
b = np.sort(a, axis= 0)
print(b)

# %%

import numpy as np

a = np.full((3, 3), 5)
print(a)

# %%

import numpy as np

a = np.eye(3)
print(a)

# %%

import numpy as np

a = np.arange(10, 19, 4)
print(a)


# %%

import numpy as np

a = np.arange(-9, 10, step= 6)
print(a)
# %%
