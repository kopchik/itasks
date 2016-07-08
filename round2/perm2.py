#!/usr/bin/env python3
from copy import copy

def perm(a):
  for i, e in enumerate(a):
    wa = copy(a)
    del wa[i]
if __name__ == '__main__':
  perm([1,2])
  
