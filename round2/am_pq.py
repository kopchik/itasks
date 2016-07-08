#!/usr/bin/env python3
import math

def check(n):
  for i in range(2, int(math.sqrt(n))+1):
    if not n%i:
      return True
  return False

if __name__ == '__main__':
  assert check(4) == True
  assert check(5) == False
  
