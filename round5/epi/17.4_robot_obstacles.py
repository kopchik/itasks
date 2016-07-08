#!/usr/bin/env python3

map = [
(0,1,0,0),
(0,0,0,0),
(0,0,1,0),
(0,0,0,0),
]
def walk(x,y, dst):
  if map[x][y] == True:
    yield False
    return
  if (x,) == dst:
    yield True
    return
  if x < dst.x:
    yield walk(x+1, y, map)
  return walk(x, y+1, map, dst)

if __name__ == '__main__':
  walk((0,0))

