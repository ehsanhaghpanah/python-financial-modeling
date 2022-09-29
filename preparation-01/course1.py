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
