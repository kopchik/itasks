#!/usr/bin/env python3


bank = [
  (50, 1),
  (10, 1),
  (5, 300)
]


class NoChange(Exception):
  pass

from functools import lru_cache

#@lru_cache(maxsize=None)
def change(s):
  if s == 0:
    return {}, 0

  coins = {}
  num = 9999999
  for coin, cnt in bank:
    i = 1
    print("trying", coin, "x", i, "to sum up to", s)
    while coin*i <= s and i <= cnt:
      try:
        c, n = change(s-i*coin)
      except NoChange:
        continue
      if n + i < num:
        num = n + i
        coins = c
        coins[coin] = coins.get(coin, 0) + i
      i += 1
  if not coins:
    raise NoChange("no change for %s" % s)
  return coins, num


if __name__ == '__main__':
  print(change(100))
  
