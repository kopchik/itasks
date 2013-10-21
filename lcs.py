#!/usr/bin/env python3
from collections import defaultdict
from copy import copy

def buildmap(l):
  m = defaultdict(list)
  for i,e in enumerate(l):
    m[e] += [i]
  return m

def lcs(a,b):
  mapa = buildmap(a)
  mapb = {}
  candidates = []  # ``bags''
  for i,sym in enumerate(b):
    apos = copy(mapa[sym])
    candidates.append(apos)
  print(candidates)
  prefixes = []
  i = 0
  while i<len(candidates):
    for c in candidates[i]:
        seq = []
        for bag in candidates[i:]:
          if c not in bag:
            break
          seq.append(c)
          bag.remove(c)
          c += 1
        print("detected seq", seq)
    i += 1

if __name__ == '__main__':
  s1 = "yyhaba"
  s2 = "haxxxhaba1"
  print(lcs(s1,s2))
