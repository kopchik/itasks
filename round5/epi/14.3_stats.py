#!/usr/bin/env python3

from collections import defaultdict
def sorted_stats(s='bcdacebe'):
  freq = defaultdict(int)
  for c in s:
    freq[c] += 1
  lower = ord('A')
  upper = ord('z')
  for code in range(lower, upper+1):
    c = chr(code)
    if c in freq:
      print(c, freq[c])


if __name__ == '__main__':
  sorted_stats()

