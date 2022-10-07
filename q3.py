
# %%

import math

def f1(l: list) -> list:
     r = [i ** 2 for i in l]
     print(r)
     pass

def f2(l: list) -> None:
     r = [i ** 2 if ((i % 2) == 0) else math.nan for i in l]
     r = [i for i in r if math.isnan(i) == False]
     print(r)
     pass

def f3(l: list) -> None:
     r = [i ** 2 if ((i % 2) == 0) else i for i in l]
     print(r)
     pass

# reverse the list
def f4(l: list) -> None:
     r = l[::-1]
     print(r)
     pass

# =============================================================

a = [2, 3, 4, 5, 6, 7, 8, 9]
f1(a)
f2(a)
f3(a)
f4(a)

# %%
