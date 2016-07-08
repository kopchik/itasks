#!/usr/bin/env python3
"""
 Given a string, find the minimum window containing a given set of characters
"""

s = "quick brown fox jumps over the lazy dog"
from collections import defaultdict
d = defaultdict(list)
[d[c].append(i) for i,c in enumerate(s)]
chars = set(['a','b','c'])

intervals = []
left = 9999999
right = 0  # (unsigned) int max
for c in chars:
  left  = min(left,  d[c][-1])
  right = max(right, d[c][0])
  intervals.append(d[c])
print(left, right, intervals)
