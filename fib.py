#!/usr/bin/env python3

def fib(n):
  if n == 1:
    return 0
  a= b = c = 1
  for x in range(2, n):
    c = a + b
    a, b = b, c
  return c


if __name__ == '__main__':
  print(fib(3))
