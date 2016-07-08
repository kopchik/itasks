#!/usr/bin/env python3

price = {
1: 1,
2: 5,
3: 8,
4: 9,
5: 10,
6: 17,
7:17,
8: 20,
9: 24,
10: 30
}

from functools import lru_cache

@lru_cache(maxsize=None)
def cut(l):
  maxprofit = 0
  for x in range(1, l+1):
    if x in price:
      maxprofit = max(maxprofit, price[x] + cut(l-x))
  return maxprofit


if __name__ == '__main__':
  print(cut(20))
  
