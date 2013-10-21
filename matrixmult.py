#!/usr/bin/env python3
from collections import OrderedDict
#matrices = OrderedDict(
#('A', (10, 30)),
#('B', (30, 5)),
#('C', (5, 60)),
#)

#matrices = ((10,30), (30,5), (5,60))
matrices = ((30,35), (35,15), (15,5), (5,10), (10,20), (20,25))

def compat(A, B):
  Ar, Ac = A
  Br, Bc = B
  return Ac == Br

def cost2(A, B):
  print("cost2",A,B)
  assert compat(A,B)
  Ar, Ac = A
  Br, Bc = B
  return Ar*Br*Bc

def combined(A,B):
  assert compat(A,B)
  Ar, Ac = A
  Br, Bc = B
  return (Ar, Bc)

cache={}
def cost(matrices=matrices):
  if matrices in cache:
    return cache[matrices]
  bestcost = 66666666666666  # INT_MAX as +infinity
  bestmatrix = None
  if len(matrices) == 1:
    return 0, matrices[0]
  if len(matrices) == 2:
    return cost2(*matrices), combined(*matrices)
  for i in range(1,len(matrices)):
    lcost, lmatrix = cost(matrices[:i])
    rcost, rmatrix = cost(matrices[i:])
    newcost = lcost+rcost+cost2(lmatrix,rmatrix)
    newmatrix = combined(lmatrix, rmatrix)
    if newcost < bestcost:
      bestcost=newcost
      bestmatrix = newmatrix
  cache[matrices] = bestcost, bestmatrix
  return bestcost, bestmatrix


if __name__ == '__main__':
  print(cost())
