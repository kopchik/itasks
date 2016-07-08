#!/usr/bin/env python3
from operator import add, truediv as div, sub

def prn1(e):
  it = e.pop(0)
  if isinstance(it, (int, float)):
    it2 = e.pop(0)
    op = e.pop(0)
    r = op(it, it2)
    e.insert(0, r)
    return r
  else:
    raise NotImplementedError

def rpn(e):
  while len(e) > 1:
    r = prn1(e)
  return r

if __name__ == '__main__':
  expr = [4, 6, div, 2, div]
  print(rpn(expr))
