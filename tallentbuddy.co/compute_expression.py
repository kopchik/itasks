#!/usr/bin/env python3

from operator import add, sub
import re

def compute_expression(expr):
  it = iter(re.findall("(\d+)|(.)",expr))
  print(calc(it))

def calc(expr):
  ops, values = [], []
  for num,op in expr:
    if num:         values.append(int(num))
    elif op == '(': values.append(calc(expr))
    elif op == ')': return calc_stack(ops, values)
    elif op == '+': ops.append(add)
    elif op == '-': ops.append(sub)
  return calc_stack(ops, values)

def calc_stack(ops, values):
  while ops:
    op = ops.pop(0)
    v1 = values.pop(0)
    v2 = values.pop(0)
    values.insert(0, op(v1,v2))
  return values.pop()



if __name__ == '__main__':
  data = "(2+2)-(3-(6-5))-4"
  # print(list(tokenize(data)))
  # print(process([add, add], [1,2,3]))
  compute_expression(data)