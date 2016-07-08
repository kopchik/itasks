#!/usr/bin/env python3

def two_numbers_sum(v, s):
  myset = set(v)
  half = s//2
  if s % 2 == 0 and half in myset:
    if len([e for e in v if e == half]) == 1:
      myset.remove(half)
  print(int(any(s-e in myset for e in v)))

if __name__ == '__main__':
  two_numbers_sum([2, 3, 4, 5, 6, 7], 14)
  
