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


def cutrod(l, cache):
  if l in cache:
    return cache[l]

  sum = 0
  maxvalue = 0
  for chunk in price:
    if chunk > l:
      continue
    value = price[chunk] + cutrod(l-chunk, cache)
    maxvalue = max(value, maxvalue)
  cache[l] = maxvalue
  return maxvalue


def cutrod2(l, price):
  val = [0 for p in price]

  for pos in range(1, l+1):
    for pos 

if __name__ == '__main__':
  print(cutrod(20, {}))
  print(cutrod(20, [1,2,3]))
