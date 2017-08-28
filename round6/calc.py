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
  expr = []
  while l:
    sym = l.pop(0)
    if sym == ')':
      break
  return _calc(expr)


def _calc(expr):
  if len(expr) == 1:
    return expr[0]

  left = expr.pop(0)
  if left == '(':
    nested = get_nested(expr)
    r = _calc(nested)
    expr.insert(0, r)
    return _calc(expr)
  op = expr.pop(0)
  right = expr.pop(0)
  print(left, op, right)
  r = op(left, right)
  expr.insert(0, r)
  return _calc(expr)

def test_calc():
  assert calc("1") == 1
  assert calc("1+2") == 3
  assert calc("1+2+3") == 6
  assert calc("1+(2+3)") == 6


if __name__ == '__main__':
  test_calc()
