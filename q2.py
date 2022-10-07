# %%

import numpy as np

def try_parse(text: str) -> float:
    try:
        return float(text)
    except:
        return None

def calculate(l: list) -> None:
     print(f'summation = {sum(l)}')
     print(f'production = {np.asarray(l).prod()}')
     print(f'subtraction = {l[0] - l[-1]}')
     pass

def main_run(quit_key: str = 'q') -> None:

     ls = []
     qk = "q" if (quit_key == None) else quit_key
     while True:
          ky = input(f"give me a number, '{qk}' to calc and quit = ")
          if ky == qk:
               if (len(ls) > 0):
                    calculate(ls)
               else:
                    print("no number entered. finished")
               break
          
          ni = try_parse(ky)
          if ni == None:
               print("not a correct number")
               continue
          
          ls.append(ni)

main_run()
