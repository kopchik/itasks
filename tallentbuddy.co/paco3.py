#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000)

class PTR:
  def __init__(self, x, y):
    self.x, self.y = x, y
  def __add__(self, other):
    return PTR(self.x + other.x, self.y + other.y)
  def __eq__(self, other):
    return (self.x, self.y) == (other.x, other.y)
  def __repr__(self):
    return "PTR(%s, %s)" %(self.x, self.y)

up    = PTR(0, -1)
down  = PTR(0, 1)
left  = PTR(-1, 0)
right = PTR(1, 0)
directions = [up, down, left, right]


def paco(data, base):
  N, M, X, K, XCa,YCa, XCo,YCo = data
  thr = int(X*K/2)
  src = PTR(XCa-1, YCa-1)
  dst = PTR(XCo-1, YCo-1)
  lightmap = [base[i*M:(i+1)*M] for i in range(N)]
  wavemap = [[None]*M for i in range(N)]

  def dump(map):
    for row in map:
      for c in row:
        print("{:2}".format(c) if c is not None else "!!", end=" ")
      print()
    print("===")

  def get(data, pos):
    return data[pos.x][pos.y]

  def validpos(pos):
    return pos.x in range(N) and pos.y in range(M)

  def trace(path):
    return sum(themap[x][y] for x,y in path)

  queue = [(src, 0)]
  while queue:
    pos, cnt = queue.pop(0)
    if not validpos(pos):
      continue
    if lightmap[pos.x][pos.y] >= K:
      continue
    if wavemap[pos.x][pos.y] is not None:
      continue
    wavemap[pos.x][pos.y] = cnt
    for d in directions:
      queue.append((pos+d, cnt+1))

  dump(lightmap)
  dump(wavemap)
  # print(get(wavemap, dst))

  cnt = get(wavemap, dst)
  acc = get(lightmap, dst)
  path = tuple()
  queue = [(dst, cnt, acc, path)]
  while queue:
    pos, cnt, acc, path = queue.pop(0)
    if not validpos(pos):
      continue
    if get(wavemap, pos) != cnt:
      continue
    acc += get(lightmap, pos)
    path = path + (pos,)
    if pos == src:
      acc2 = sum(get(lightmap, p) for p in path)
      print(cnt, acc, acc2, path)
    for d in directions:
      queue.append((pos+d, cnt-1, acc, path))


if __name__ == '__main__':
  data = [4,4,3,7,1,1,4,4]
  base = [1,1,4,4,0,4,4,4,7,3,2,3,14,9,8,3]
  # from pacodata import data, base
  #data = [2,2, 10, 10, 1,1, 2,2]
  #base = [0,0,0,0]
  paco(data, base)
