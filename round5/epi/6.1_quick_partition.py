#!/usr/bin/env python3


def part(l, pos):
  pivot = l[pos]
  j = len(l) - 1
  for i,e in enumerate(l):
    if i >= j:
      break
    if e < pivot:
      continue
    while l[j] > pivot and j>0:
      j -= 1
    if j <= i:
      break
    print("swapping", l[i], l[j])
    l[i] = l[j]
    l[j] = e
  return l

if __name__ == '__main__':
  print(part([3,0,5,1,3,3,2,4], 3))
  
