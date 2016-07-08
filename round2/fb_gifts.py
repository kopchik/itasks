#!/usr/bin/env python3
# Given a 2D array of gifts, find path from top left to bottom right corner with greatest aggregated gift values.

from collections import namedtuple
#import sys
#sys.setrecursionlimit(90)

class XY(namedtuple('XY', ['x', 'y'])):
  def __add__(self, other):
    print("adding {} to {}".format(self, other))
    return XY(self.x+other.x,
              self.y+other.y)


giftmap = [
[1,2,3],
[0,4,5],
[7,8,1],
]
dimentions = XY(2,2)
directions = [XY(1,0), XY(0,1), XY(-1,0), XY(0,-1)]


def go(pos, path, value, dst=(2,2)):
  """ pos  -- position to walk to
      path -- path walked so far
      value -- sum of the path

      Returns value of the path (-1 if path is invalid)
  """
  print(pos, value, path)
  if not (0 <=pos.x <= dimentions.x
          and 0 <= pos.y <= dimentions.y):
          return -1, ()
  if pos in path:
    return -1, ()  # this point has already been visited
  value += giftmap[pos.y][pos.x]
  path = path + (pos,)
  if pos == dst:
    return value, path
  return max(
      (go(pos+vector, path, value, dst)
        for vector in directions),
        key = lambda x: x[0]
      )


if __name__ == '__main__':
  print(go(pos=XY(0,0),
           path=(),
           value=0,
           dst=XY(2,2)))

