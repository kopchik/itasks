#!/usr/bin/env python3

import operator


def calc(s):
  expr = []
  for e in s:
    if e.isnumeric():
      expr.append(int(e))
    elif e in ['(', ')']:
      expr.append(e)
    elif e == '+':
      expr.append(operator.add)
  return _calc(expr)


def get_nested(l):
  if l[0] != '(':
    return [l.pop(0)]

  expr = []
  while l:
    sym = l.pop(0)
    if sym == ')':
      break
  return expr


def _calc(l):
  if len(l) == 1:
    return l[0]
  left = _calc(get_nested(l))
  if not l:
    return left
  op = l.pop(0)
  right = _calc(get_nested(l))
  print(left, op, right)


def test_calc():
  assert calc("1") == 1
  assert calc("1+2") == 3


if __name__ == '__main__':
  test_calc()
