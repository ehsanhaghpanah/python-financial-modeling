# %%

def main_run(quit_key: str = 'q') -> None:

     # row = 1,2,3,4,5,6,7,8
     # col = a,b,c,d,e,f,g,h

     qk = "q" if (quit_key == None) else quit_key
     row = ''
     while True:
          row = input(f"give me row (1,2,3,4,5,6,7,8), '{qk}' to quit = ")
          if row == qk:
               print("finished")
               exit()
          elif (len(row) == 1) and (row in '12345678'):
               break
          else:
               print("give me correct row. something like 1,2,3,4,5,6,7,8")
               continue
               
     col = ''
     while True:
          col = input(f"give me col (a,b,c,d,e,f,g,h), '{qk}' to quit = ")
          if col == qk:
               print("finished")
               exit()
          elif (len(col) == 1) and (col in 'abcdefgh'):
               break
          else:
               print("give me correct col. something like a,b,c,d,e,f,g,h")
               continue

     flag = ord(col) % 2 ^ int(row) % 2
     if flag:
          print(f'position ({col}, {row}) is white')
     else:
          print(f'position ({col}, {row}) is black')

main_run()



