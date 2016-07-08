#!/usr/bin/env python3

def findNonRepChar(s):
  counts = {}
  positions = {}
  for pos, c in enumerate(s):
    if c not in counts:
      counts[c] = 1
      positions[c] = pos
    else:
      counts[c] = counts[c] + 1

  for c,pos in sorted(positions.items()):
    if counts[c] > 1:
      continue
    return c
  return None
