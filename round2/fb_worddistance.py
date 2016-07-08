#!/usr/bin/env python3

from functools import lru_cache

maxdist = 2
@lru_cache(maxsize=None)
def distance(a, b, dist=0):
  if not a: return dist+len(b)
  if not b: return dist+len(a)
  if a[0] != b[0]:
    dist += 1
  r = min(
    distance(a, b[1:], dist+1),
    distance(a[1:], b, dist+1),
    distance(a[1:], b[1:], dist)
  )
  return r if r <= maxdist else 999999

if __name__ == '__main__':
  r = distance('cat', 'katrt')
  print(r)
