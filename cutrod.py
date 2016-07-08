#!/usr/bin/env python3
from functools import wraps
from time import time

def timed(f):
  @wraps(f)
  def wrapper(*args, **kwds):
    start = time()
    result = f(*args, **kwds)
    elapsed = time() - start
    print("%s took %d time to finish" % (f.__name__, elapsed))
    return result
  return wrapper

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

r = [None for _ in range(10000)]
@timed
def cut(length):
  if length == 0:
    return 0
  if r[length]:
    return r[length]
  profit = 0
  for n in range(1, length+1):
    if n > 10: n=10
    profit = max(profit, price[n]+cut(length-n))
  r[length] = profit
  return profit

@timed
def cut2(len):
  r = [0]*(len+2)
  profit = 0
  for i in range(1, len+1):
    for j in range(1, i+1):
      profit = max(profit, price.get(j,0) + r[i-j])
    r[i] = profit
  return profit



if __name__ == '__main__':
  n = 100
  assert cut(n) == cut2(n)
  print(cut(20))
