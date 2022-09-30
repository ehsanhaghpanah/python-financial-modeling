# %%

import numpy as np

a = list(range(1, 1_000_000))
b = [i * 5 for i in a]

x = np.arange(start= 1, stop= 1_000_000)
y = [i * 5 for i in x]

print(b == y)

# %%

#
# one dimentional array

import numpy as np

x = np.array([1, 2, 3, 4, 5, True])
print(f'array = {x}')
print(f'array N dimension = {x.ndim}')
print(f'array shape = {x.shape}')
print(f'array size = {x.size}')
print(f'array len = {len(x)}')
print(f'array data type = {x.dtype}')

# %%

#
# two dimentional array

import numpy as np

x = np.array([[1, 2], [2, 1]])
print(f'array = {x}')
print(f'array N dimension = {x.ndim}')
print(f'array shape = {x.shape}')
print(f'array size = {x.size}')
print(f'array len = {len(x)}')
print(f'array data type = {x.dtype}')

# %%

# 
# differnce between multiplication in list and matrices

import numpy as np

a = [1, 2, 3, 4, 5]
b = a * 2
print(b)

x = np.array([1, 2, 3, 4, 5])
y = x * 2
print(y)

# %%

# arithmatic operation(s) on numpy arrays

a = np.array([1, 2, 3, 4, 5])
b = a + 1
print(b)

# %%

#
# matrics multiplications

import numpy as np

a = np.array([1, 2])
b = np.array([[2, 3], [3, 4]])
c = np.dot(a, b)
print(c)

# %%

# transposition

import numpy as np

a = np.array([[1, 2], [3, 4]])
b = a.T

print(b)

# %%

a = np.array([1, 2, 3, 4, 5])
b = a.T

# print(a.shape)
# print(b.shape)
print(a)
print(b)


# %%

a = np.array([[1, 2], [3, 4], [5, 6]])
b = a.T

print(a)
print(b)

print(a.shape)
print(b.shape)
# %%

a = np.array([1, 2, 3, 5, 5])
b = np.array([1, 1, 3, 4, 5])

c = (a > b)
print(c)

# %%

import numpy as np

a = np.array([7, 2, 3, 4, 5])
print(a.max())
print(a.min())
print(a.sum())
print(a.mean())
print(a.argmax())
print(a.argmin())


# %%

# a = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 0], [1, 2, 3, 4, 5]])
a = np.array([[0, 0, 0, 0, 5], [6, 7, 8, 9, 0], [1, 2, 3, 4, 5]])

print(a.max())
print(a.min())
print(a.sum())
print(a.mean())
print(a.argmax())
print(a.argmin())

print(a.sum(axis=0))

# %%

b = np.ones((3, 3))
print(b)

# %%

b = np.zeros((3, 3))
print(b)


# %%

a = np.array([[1, 2], [3, 4]])
print(a.sum(axis= 1))

# %%

import numpy as np

a = np.array([[1, 2], [3, 4]])
print(f'cols summation = {a.sum(axis= 0)}')
print(f'rows summation = {a.sum(axis= 1)}')


# %%
