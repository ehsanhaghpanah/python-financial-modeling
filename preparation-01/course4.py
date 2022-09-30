# %%

import numpy as np
import matplotlib.pyplot as pl
import scipy as sp

a = np.array([.01, .05, .02, .01, .04])
b = np.array([.07, .01, .02, .02, .02])

c = (a == b)
u = np.unique(c, return_counts= True)

print(u)

# %%

# x = np.random.randint(1, 7, 2).sum()
# def sum_dice():
#      return np.random.randint(1, 7, 2)

def sum_dice(dice_number = 2):
     return np.random.randint(1, 7, dice_number).sum() 

a = [sum_dice() for i in range(1_000_000)]
ue, uc = np.unique(a, return_counts= True)

# print(f'unique e = {ue}')
# print(f'unique c = {uc}')

x = ue
y = uc

pl.plot(x, y)
pl.show()

# %%
