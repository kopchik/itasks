#!/usr/bin/env python3
from itertools import permutations

def robo2(m,n):
  if m == 0 and n== 0: return 1
  a = 0
  if m:
    a += robo2(m-1,n)
  if n:
    a += robo2(m, n-1)
  return a

def robo2(m,n):
  if m<0 or n<0: return 0
  if m == 0 and n== 0: return 1
  a = 0
  if m:
    a += robo2(m-1,n)
  if n:
    a += robo2(m, n-1)
  return a

def robo3(m,n):
  print(m,n)
  if m == 0 and n == 0:
    print("OPA")
    return 1
  return robo3(m-1,n) if m else 0 + \
         robo3(m, n-1) if n else 0


cache = {}
def solve(i, j):
  if (i,j) in cache:
    return cache[(i,j)]
  if j == 0 and i == 0:
    sol = 1
  elif i == 0:
    sol = solve(i, j-1)
  elif j == 0:
    sol = solve(i-1, j)
  else:
    sol = solve(i-1, j) + solve(i, j-1)
  cache[(i,j)] = sol
  return sol




if __name__ == '__main__':
    print(robo2(3,3))
    print(solve(3,3))
