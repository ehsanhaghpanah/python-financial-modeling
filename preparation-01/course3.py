# %%

import numpy as np

def f(x):
     return x ** 2

a = np.arange(-3, 4)
b = f(a)
print(b)

print(f(a).max())
print(f(a).min())
print(f(a).mean())
print(f(a).argmax(axis= 0))
print(f(a).argmin())

# %%


