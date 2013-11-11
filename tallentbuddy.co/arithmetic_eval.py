#!/usr/bin/env python3
from operator import mul, sub, add, floordiv
import re

symap = {'+': add, '-': sub, '*': mul, '/': floordiv}
opmap = {sub: 10, add: 10, mul: 5, '/': 5, '(': 1, ')': 1}
revmap = {v:k for k, v in symap.items()}

def arithmetic_eval(expr):
  syms = re.findall("(\d+|[-+*/()])", expr.replace(" ",""))
  expr = [symap[s] if s in symap else int(s) if s.isnumeric() else s for s in syms]
  return calc(iter(expr))

def calc(syms):
  ops = []
  queue = []
  for sym in syms:
    if sym == '(':
      s.append(calc_queue(queue))
    elif sym == ')':
      return calc_queue(queue)
    elif sym in opmap:
      op = opmap[sym]
      while ops:
        if opmap[ops[-1]] <= op:
          queue.append(ops.pop())
          continue
        break
      ops.append(op)
    else:
      queue.append(sym)
  if ops: queue += reversed(ops)
  return calc_queue(queue)

def calc_queue(queue):
  print(queue)
  stack = []
  while len(queue):
    sym = queue.pop(0)
    if isinstance(sym, int):
      stack.append(sym)
    else:
      right = stack.pop()
      left  = stack.pop()
      r = sym(left,right)
      print(left, revmap[sym], right, '=', r)
      stack.append(r)
  return r



#expr = [symap[s] if s in symap else s for s in syms]
if __name__ == '__main__':
  #print(arithmetic_eval("( 1+2 ) *4"))
  #print(arithmetic_eval("2 + 3 * ( 1 - 4*2)"))
  #assert arithmetic_eval("1 + 0 - 0  * 1 + 2 * 2 * (2)") == 9
  assert arithmetic_eval("1 - 1 - 1") == -1
  assert arithmetic_eval("1 - 2 * 3") == -5
  #arithmetic_eval("1-2*3")

