import sys
import math

def main():
  limit = int(sys.argv[1])
  res = 1
  i = 0
  se = 3
  sw = 5
  nw = 7
  j = 3
  while i<limit:
    #print j
    res = res + j**2
    res = res + (se + sw + nw)
    se = se + 2*(2*j-1)
    sw = sw + 2*(2*j)
    nw = nw + 2*(2*j+1)
    j = j + 2
    i = i + 1
  print res

if __name__ == "__main__":
  main()
