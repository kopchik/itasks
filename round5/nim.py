#!/usr/bin/env python3

def canwin(n, me=True):
  for take in [1,2,3]:
    rest = n - take
    if rest == 0:
      return me
    return canwin(rest, not me)

if __name__ == '__main__':
  print(canwin(1348820612))
  
