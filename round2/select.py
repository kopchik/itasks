#!/usr/bin/env python3

def select(l, k):
  print("select", k, "from", l)
  if k == 0:
    return []
  pivot = l[0]
  left  = [e for e in l if e<=pivot]
  right = [e for e in l if e>pivot]
  print(left, right)
  if len(left) > k:
    return select(left, k)
  else:
    return left + select(right, k-len(left))

if __name__ == '__main__':
  l = [1,2,35,4,7,2,3,4]
  print(select(l, 3))
