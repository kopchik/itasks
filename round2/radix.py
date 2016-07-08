#!/usr/bin/env python3
from math import log, ceil

def radix(a, w, i=None):
  if i is None:
    i = 32-w   # where 32 is the maximum width
  if i < 0 or len(a) == 1:
    return a
  buckets = [[] for i in range(2**w)]
  mask = (2**w - 1) << i
  print("mask: ", bin(mask), "shift:", i)
  for e in a:
    idx = (e & mask) >> i
    buckets[idx].append(e)
  r = []
  print(buckets)
  for b in buckets:
    if not b:
      continue
    r.extend(radix(b, w, i-w))
  return r


if __name__ == '__main__':
  data = [3,2,5,4,6,1, 10]
  width = 8
  digits = ceil(log(max(data), 2**3))
  r = radix(data, width, width*digits)
  print(r)
