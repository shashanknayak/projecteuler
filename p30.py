import sys

def find_sum():
 res = 0
 for i in range(0,10):
   for j in range(0,10):
     for k in range(0,10):
       for l in range(0,10):
         for m in range(0,10):
           for o in range(0,10):
             num = 100000*i + 10000*j + 1000*k + 100*l + 10*m + o
             if num>295245:
               return res

             if num == (i**5 + j**5 + k**5 + l**5 + m**5 + o**5):
               res = res + num

def main():
  print find_sum()-1

if __name__ == "__main__":
  main()
