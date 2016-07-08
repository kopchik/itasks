#!/usr/bin/env python3

def move(l):
  for idx1, e in enumerate(l):
    if e == 0:
      break
  else:
    return l
  idx2 = idx1 + 1
  while True:
    print(l)
    if idx2 == len(l):
      break
    if l[idx2] == 0:
      idx2 += 1
      continue
    l[idx1], l[idx2] = l[idx2], l[idx1]
    idx1 += 1
    idx2 += 1
  return l

def move2(l):
  idx1,idx2 = 0, 0
  while True:
    print(l)
    if idx2 == len(l):
      break
    if l[idx2] != 0:
      l[idx1], l[idx2] = l[idx2], l[idx1]
      idx1 += 1
      idx2 += 1
    else:
      idx2 += 1
  return l


if __name__ == '__main__':
  data = [0,0,0,8,3]
  print(move2(data))
