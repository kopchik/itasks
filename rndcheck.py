#!/usr/bin/env python3

def partition(l):
  r = []
  subseq = []
  for a,b in zip(l, l[1:]):
    print(a,b)
    subseq.append(a)
    if a != b:
      r.append(subseq)
      subseq = []
  if subseq:
    r.append(subseq)
  return r

if __name__ == '__main__':
  r = partition([1,1,2,2,1,3,3,3,4])
  print(r)
  
