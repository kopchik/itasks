#!/usr/bin/env python3
import re
from operator import mul, sub, add
symap = {'+': add, '-': sub, '*': mul}
opmap = {sub: 10, add: 10, mul: 5, '/': 5, '(': 1, ')': 1}
def arithmetic_eval(expr):
  syms = re.findall("(\d+|[-+*/()])", expr.replace(" ",""))
  expr = [symap[s] if s in symap else s for s in syms]
  expr = [symap[s] if s in symap else int(s) if s.isnumeric() else s for s in syms]
  return calc(iter(expr))

def calc(syms):
  ops = []
  nums = []
  for sym in syms:
    if sym == '(':
      nums.append(calc(syms))
    elif sym == ')':
      return stack(ops, nums)
    elif sym in opmap:
      if not ops or opmap[sym] < opmap[ops[-1]]:
        ops.append(sym)
      else:
        v = stack(ops, nums)
        nums.append(v)  #TODO:
    else:
      nums.append(sym)
  return stack(ops, nums)

def stack(ops, nums):
  while ops:
    op = ops.pop()
    right = nums.pop()
    left = nums.pop()
    print(left, op, right)
    r = op(left, right)
    nums.append(r)
  return nums[0]


if __name__ == '__main__':
  #print(arithmetic_eval("( 1+2 ) *4"))
  print(arithmetic_eval("2 + 3 * ( 1 - 4*2)"))


