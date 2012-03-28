import math
import sys

def main():
  limit = int(sys.argv[1])
  max_recur_len = 0
  max_recur_cyc = 0
  for i in reversed(range(2,limit)):
    j = 1
    while j<i:
      if (10**j)%i == 1:
        if max_recur_len<j:
          max_recur_len = j
          max_recur_cyc = i
        #print i, j
        break
      j=j+1
  print max_recur_cyc

if __name__=="__main__":
  main()

