#!/usr/bin/env python3

def gcd(m, n):
  while n:
    r = m%n
    m,n = n,r
  return m


if __name__ == '__main__':
  print(gcd(32, 11))
