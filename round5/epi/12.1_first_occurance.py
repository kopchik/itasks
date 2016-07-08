#!/usr/bin/env python3


def search(l, e):
  left = 0
  right = len(l) -1
  while left != right:
    pos = (right - left) // 2
    e2 = l[pos]
    if e2 > e:
      left = pos
    elif e2 < e:
      righ = pos
    else:
      break

  while True:
    if pos and l[pos-1] == e:
      pos -= 1
      continue
    break
  return pos


if __name__ == '__main__':
  
  
