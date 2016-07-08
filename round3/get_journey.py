#!/usr/bin/env python3

def get_journey(src, dst):
  # build itenary graph
  g = {s:d for s,d in zip(src, dst)}

  # find original departure
  point = [p for p in src if p not in dst][0]
  while point is not None:
    print(point)
    point = g.get(point, None)


if __name__ == '__main__':
  get_journey([1, 4, 5], [2, 1, 4])

