#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000)

def paco(data, base):
  N, M, X, K, XCa,YCa, XCo,YCo = data
  dst = (XCo-1, YCo-1)
  thr = int(X*K/2)
  themap = [base[i*M:(i+1)*M] for i in range(N)]

  def trace(path):
    return sum(themap[x][y] for x,y in path)

  invalid = (M*N+1,6666)
  cache = [invalid for x in base]
  def visit(x,y, length=0, risk=0):
    idx = x+N*y
    # out of map
    if not (0 <= x < N and 0 <= y < M):
      return invalid
    # too brigh square
    k = base[idx]
    if k > K:
      return invalid
    risk += k
    # area already cached
    if cache[idx] < (length, risk):
      return invalid
    cache[idx] = (length, risk)
    if (x,y) == dst:
      print("dst", length, risk)
      return length, risk
    r = min(visit(x+1, y, length+1, risk),
            visit(x-1, y, length+1, risk),
            visit(x,y+1, length+1, risk),
            visit(x, y-1, length+1, risk))
    return r
  print(visit(XCa-1,YCa-1))




if __name__ == '__main__':
  data = [4,4,3,7,1,1,4,4]
  base = [1,1,4,4,0,4,4,4,7,3,2,3,14,9,8,3]
  from pacodata import data, base
  #data = [2,2, 10, 10, 1,1, 2,2]
  #base = [0,0,0,0]
  paco(data, base)
