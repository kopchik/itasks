#!/usr/bin/env python3
from __future__ import print_function

cache = {}
def maxsum(v):
  if v in cache:
    return cache[v]
  answer = 0
  i = 0
  while i<len(v):
    answer = max(answer,v[i]+maxsum(v[i+2:]))
    i += 1
  cache[v] = answer
  return answer

def find_max_sum2(v):
  print(maxsum(tuple(v)))

def find_max_sum(v):
    s1, s2 = 0, 0
    for i in range(len(v)):
        s = max(s1, s2 + v[i])
        s2 = s1
        s1 = s
    print(s1)

if __name__ == '__main__':
    v= [2, 6, 7, 8]
  assert find_max_sum(v) == find_max_sum2(v)
