#!/usr/bin/env python3
# 1005. Stone Pile http://acm.timus.ru
from itertools import combinations
from copy import copy
import sys

l = int(sys.stdin.readline())
stones = [int(d) for d in sys.stdin.read().split()]
#stones = [5, 8, 13, 27, 14]
assert l == len(stones)
answer = None
for r in range(1, l+1):
  for p1 in combinations(stones, r):
    p2 = copy(stones)
    for x in p1:
      p2.remove(x)
    diff = abs(sum(p1) - sum(p2))
    if not answer or diff < answer:
      answer = diff
print(answer)
