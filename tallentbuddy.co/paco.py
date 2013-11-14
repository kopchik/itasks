#!/usr/bin/env python3

def paco(data, base):
  N, M, X, K, XCa,YCa, XCo,YCo = data
  themap = []
  cur = (XCa-1, YCa-1)
  dst = (XCo-1, YCo-1)
  for i in range(M):
    themap.append(base[i*N:(i+1)*N])
  print(themap)
  def move(cur, inc):
    return list(map(sum, zip(a,b)))
  def travel(cur, path=()):
    if cur == dst:  return path + (cur,)
    if cur in path: return False
    x,y = cur
    if themap[x][y] >= K:
      return False
    r = []



if __name__ == '__main__':
  data = [4,4,3,7,1,1,4,4]
  base = [1,1,4,4,
          0,4,4,4,
          7,3,2,3,
          14,9,8,3]
  paco(data, base)

