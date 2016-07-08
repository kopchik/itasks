#!/usr/bin/env python3

def partition(l, predicate):
  left, right = [], []
  for e in l:
    left.append(e) if predicate(e) else right.append
  return left, right

if __name__ == '__main__':
  data = [0, 1, -1]
  s = set()
  cum = 0
  #for e in data:
  #  cum += e
  #  if cum in s:
  #    print("!")
  #  s.add(cum)
  positive, negative = partition(data, lambda x: x>0)
    
