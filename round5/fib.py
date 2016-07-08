#!/usr/bin/env python3


def fib(n):
  if n < 2:
    return n
  return fib(n-1) + fib(n-2)

cache = {}
def fib(n):
  assert n >= 1, "n should be >= 1"
  if n in cache:
    return cache[n]
  if n <= 2:
    return 1
  res = fib(n-1) + fib(n-2)
  cache[n] = res
  return res

def fib(n):
  res = [0 for x in range(n+1)]
  res[0] = 0
  res[1] = 1
  res[2] = 1
  for x in range(2,n+1):
    res[x] = res[x-1] + res[x-2]
  print(res)

if __name__ == '__main__':
  print(fib(14))
