#!/usr/bin/env python3

def subset(l):
  l.sort()
  min = 0
  max = 1
  #l = [0,1,2,6, None]
  l = [0, 1, 2, 3]
  #l = [-6, 0, 1, 2]
  pairs = zip(l[:-1],l[1:])
  for pos, (i, j) in enumerate(pairs, 1):
    #print(i, j)
    if i+1 != j:
      if max - min < pos - max:
        min = max
        max = pos
    print(len(l), pos)
  print(l)
  return l[min:max]


if __name__ == '__main__':
  l = [3, -2, 7, 9, 8, 1, 2, 0]
  print(subset(l))
