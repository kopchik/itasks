#!/usr/bin/env python3


def jump(n):
  assert n >= 0
  if n <= 2:
    return n
  r = [0 for x in range(n+1)]
  r[1] = 1
  r[2] = 2
  for x in range(3,n+1):
    r[x] = r[x-1] + r[x-2]
  print(r)
  return r[-1]  # last elem

if __name__ == '__main__':
  print(jump(10))
  
