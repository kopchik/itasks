#!/usr/bin/env python3
from collections import Counter

def is_poli(s):
  counter = Counter(s)
  odd = 0
  for c, cnt in counter:
    if cnt%2:
      odd += 1
  return odd <= 1


if __name__ == '__main__':
  is_poli('test')
  
