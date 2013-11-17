#!/usr/bin/env python3

def paco(data, base):
  N, M, X, K, XCa,YCa, XCo,YCo = data
  pos = (XCa-1, YCa-1)
  dst = (XCo-1, YCo-1)
  thr = int(X*K/2)
  themap = [base[i*N:(i+1)*N] for i in range(M)]

  def move(pos, inc):
    return tuple(map(sum, zip(pos, inc)))

  def trace(path):
    return sum(themap[x][y] for x,y in path)

  def visit(pos=pos, path=()):
    if pos in path: return []
    path = path + (pos,)
    if pos == dst: return [path]  # we reached destination
    x,y = pos
    if  x not in range(N) \
     or y not in range(M) \
     or themap[x][y] >= K \
     or trace(path[-X:]) >= thr:
      return []
    r = visit(move(pos,(1,0)), path) \
         + visit(move(pos,(-1,0)), path) \
         + visit(move(pos,(0,1)), path) \
         + visit(move(pos,(0,-1)), path)
    return [min(r, key=lambda l: len(l))] if r else []
  path = visit()[0] # [0]
  #[print(m) for m in themap]
  print(len(path)-1, trace(path))




if __name__ == '__main__':
  data = [4,4,3,7,1,1,4,4]
  base = [1,1,4,4,0,4,4,4,7,3,2,3,14,9,8,3]
  paco(data, base)
