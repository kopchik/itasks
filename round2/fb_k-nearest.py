#!/usr/bin/env python3

from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])

def nearest(loc, points, k):
  def distance(point):
    return   (loc.x-point.x)**2  \
           + (loc.y-point.y)**2
  points.sort(key=distance, reverse=True)
  return points[-k:]


if __name__ == '__main__':
  points = [
    Point(1,1),
    Point(2,1),
    Point(4,10),
  ]
  print(nearest(loc=Point(0,0), points=points, k=2))
