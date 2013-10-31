#!/usr/bin/env python3
import re
from operator import mul, sub, add, floordiv
symap = {'+': add, '-': sub, '*': mul, '/': floordiv}
opmap = {sub: 10, add: 10, mul: 5, '/': 5, '(': 1, ')': 1}
def arithmetic_eval(expr):
  syms = re.findall("(\d+|[-+*/()])", expr.replace(" ",""))
  #expr = [symap[s] if s in symap else s for s in syms]
  expr = [symap[s] if s in symap else int(s) if s.isnumeric() else s for s in syms]
  return calc(iter(expr))

def calc(syms):
  ops = []
  nums = []
  for sym in syms:
    if sym == '(':
      nums.append(calc(syms))
    elif sym == ')':
      return calc_stack(ops, nums)
    elif sym in opmap:
      if not ops or opmap[sym] <= opmap[ops[-1]]:
        ops.append(sym)
      else:
        v = calc_stack(ops, nums)
        nums.append(v)  #TODO:
    else:
      nums.append(sym)
  return calc_stack(ops, nums)

def calc_stack(ops, nums):
  print(ops, nums, end=' ')
  while ops:
    op = ops.pop()
    right = nums.pop()
    left  = nums.pop()
    nums.append(op(left,right))
  print(nums[-1])
  return nums[-1]


if __name__ == '__main__':
  #print(arithmetic_eval("( 1+2 ) *4"))
  #print(arithmetic_eval("2 + 3 * ( 1 - 4*2)"))
  print(arithmetic_eval("1 + 0 - 0  * 1 + 2 * 2 * (2)"))


