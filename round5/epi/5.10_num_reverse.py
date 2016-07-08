#!/usr/bin/env python3


def numrev(num):
  # TODO: we could convert in-place and not use digits array
  assert num >= 0

  result = 0
  while num:
    result = result*10 + num%10
    num //= 10
  return result

if __name__ == '__main__':
  test = [0, 123, 1, 10, 11, 101, 99]
  print([(t, numrev(t)) for t in test])
  
