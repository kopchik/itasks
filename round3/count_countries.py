#!/usr/bin/env python3

from pprint import pprint

def walk(x,y, g):
  """ ``Paint'' the country on map. """
  sym = g[x][y]
  q = [(x,y)]
  while q:
    x,y = q.pop(0)
    if x<0 or x >= len(g):
      continue
    if y<0 or y >= len(g[0]):
      continue
    if g[x][y] != sym:
      continue
    g[x][y] = 'x'
    q.extend([(x-1,y),(x+1,y),
              (x,y-1),(x,y+1)])

def find(g):
  """ Find next untraversed point of map. """
  for x, line in enumerate(g):
    for y, sym in enumerate(line):
      if sym != 'x':
        yield (x,y)

def count_countries(g):
  # mutable map
  g = [list(line) for line in g]
  for cnt, (x, y) in enumerate(find(g), 1):
    walk(x, y, g)
  print(cnt)

if __name__ == '__main__':
  g = ["11123",
       "12223",
       "32333",
       "11122",
       "22333"]
  count_countries(g)
