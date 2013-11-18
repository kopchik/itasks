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
  dst = (XCo-1, YCo-1)
  thr = int(X*K/2)
  themap = [base[i*M:(i+1)*M] for i in range(N)]
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

  startpos = PTR(XCa-1, YCa-1)
  endpos = PTR(XCo-1, YCo-1)

  queue = [(startpos, 0)]
  while queue:
    pos, cnt = queue.pop(0)
    if not validpos(pos):
      continue
    if themap[pos.x][pos.y] >= K:
      continue
    if wavemap[pos.x][pos.y] is not None:
      continue
    wavemap[pos.x][pos.y] = cnt
    for d in directions:
      queue.append((pos+d, cnt+1))

  dump(themap)
  dump(wavemap)
  print(get(wavemap, endpos))

  cnt = get(wavemap, pos)
  acc = get(themap, pos)
  queue = [(endpos, cnt, acc)]
  while queue:
    pos, cnt, acc = queue.pop(0)
    if not validpos(pos):
      continue
    if pos == endpos:
      print(cnt, acc)
    if get(wavemap, pos) != cnt:
      continue
    acc += get(themap, pos)
    for d in directions:
      queue.append((pos+d, cnt-1, acc))


if __name__ == '__main__':
  data = [4,4,3,7,1,1,4,4]
  base = [1,1,4,4,0,4,4,4,7,3,2,3,14,9,8,3]
  from pacodata import data, base
  #data = [2,2, 10, 10, 1,1, 2,2]
  #base = [0,0,0,0]
  paco(data, base)
