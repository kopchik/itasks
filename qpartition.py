#!/usr/bin/env python3

def part(l, e):
  size = len(l)
  i = 0
  j = size - 1
  while i < j:
    if l[i] > e:
      while j > i and l[j] > e:
        j -= 1
      l[i], l[j] = l[j], l[i]
      j -= 1
    i += 1
  print(l)
  return l[:i], e, l[i:]

print(part([7,6,5,4,3,2,9,9], 4))
