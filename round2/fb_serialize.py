#!/usr/bin/env python3
import re
import sys


def ser(tree):
  v, l, r = tree
  l = ser(l) if l else None
  r = ser(r) if r else None
  return "[ {v} {l} {r} ]"  \
    .format(v=v, l=l, r=r)


def deser(it):
  values = []
  for e in it:
    if e == '[':
      values.append(deser(it))
    elif e == ']':
      return values
    elif e == 'None':
      values.append(None)
    else:
      values.append(int(e))
  return values


if __name__ == '__main__':
  tree = [1, [2, None, None], [3, None, None]]
  r = ser(tree)
  print(r)
  it = iter(r.split()[1:])
  r = deser(it)
  print(r)
  assert tree == r
