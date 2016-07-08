#!/usr/bin/env python3
from functools import lru_cache

@lru_cache(maxsize=None)
def stairs(n):
  if n < 3:
    return n
  else:
    return stairs(n-1) + stairs(n-2)

#0 => 0
#1 => 1
#2 =>
#  1 + stairs(1)
#  2 + stairs(0)

assert stairs(0) == 0
assert stairs(1) == 1
assert stairs(2) == 2
print(stairs(3))
