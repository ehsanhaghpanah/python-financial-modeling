
# %%

import numpy as np
import matplotlib.pyplot as pl

names  = ['aa', 'bb', 'cc', 'dd']
values = [2523, 3620, 8400, 6230]

def absolute_value(val):
    a  = np.round(val/100. * np.sum(values), 0)
    return a

pl.subplot(221)
explodes = [0, 0, 0.1, 0.5]
pl.pie(values, labels= names, shadow= True, autopct= absolute_value, explode= explodes, startangle= 90)
# pl.pie(values, labels= names, autopct= "%1.0f%%", shadow= True, explode= explodes, startangle= 90)
pl.show()

pl.subplot(222)
pl.barh(names, values)
pl.title("nm")
pl.show()

pl.subplot(212)
pl.plot(values)
pl.show()

# %%

import numpy as np

arr = np.array([2, 3, 5, 8, 9,4])
print(np.percentile(arr, 25))
print(np.percentile(arr, 50))
print(np.percentile(arr, 75))
