#!/usr/bin/env python3

def find(l):
  min, max = 0, len(l)-1
  for _ in range(6):
    print(min, max)
    pos = (min+max) // 2
    e = l[pos]
    if min + 1 == max:
      return e
    elif pos > 0 and l[pos-1] < e:
      max = pos
    elif pos < len(l)-1 and l[pos+1] > e:
      min = pos


if __name__ == '__main__':
  l = [378,478,550,631,103,203,220,234,279,368]
  l = list(range(10))
  print(find(l))
