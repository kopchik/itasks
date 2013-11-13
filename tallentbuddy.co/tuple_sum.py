#!/usr/bin/env python3
from collections import defaultdict


def tuple_sum(a,s):
  candidates = ts(a,s)
  best = candidates[0]
  for c in candidates:
    print(c)
    if len(c) < len(best):
      best = c
    elif len(c) == len(best):
      #print(c, best)
      pass

def ts(a, s, pos=0):
  off=pos
  if s == 0: return [[]]
  if pos == len(a): return []
  answers = []
  while pos < len(a):
    e = a[pos]
    for answer in ts(a, s-e, pos+1):
      answers.append([e]+answer)
    pos += 1
  return answers


if __name__ == '__main__':
  a,s = list(map(int, "3 2 1 4 5 7 6 9 7 8".split())), 30
  #tuple_sum(a, s=30)
  #a, s = [1,3,1], 4
  tuple_sum(a, s)
  #ts(a, s)
