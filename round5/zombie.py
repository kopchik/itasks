#!/usr/bin/env python3
from collections import defaultdict

themap = \
"""
1100
1100
0010
0001
"""

def lookup(table, i,j):
  if table[i][j] == '1':
    return True
  return False


def clusters(table):
  num_zombies = len(table)
  zombie_map = defaultdict(list)
  for zombie in range(num_zombies):
    for other in range(num_zombies):
      if lookup(table, zombie, other):
        zombie_map[zombie].append(other)

  seen = set()
  num_clusters = 0
  for zombie in range(num_zombies):
    if zombie in seen:
      continue
    num_clusters += 1
    queue = [zombie]
    while True:
      print(seen, queue)
      if not queue:
        break
      zombie = queue.pop(0)
      seen.add(zombie)
      for other in zombie_map[zombie]:
        if other not in seen:
          queue.append(other)

  print(zombie_map)
  print(num_clusters)


if __name__ == '__main__':
  print(clusters(themap.strip().splitlines()))
  
