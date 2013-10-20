#!/usr/bin/env python3

_counter = 0
def skip(it, num):
  for x in range(num):
    next(it)

class enum:
  def __init__(self, it, skip=0, stop=None):
    # cut tail
    if stop and stop < 0:
      stop = len(it) + stop
    self.stop = stop
    # skip
    it = enumerate(it)
    for x in range(skip):
      next(it)
    self.it = it
  def __iter__(self):
    return self
  def __next__(self):
    i, e = next(self.it)
    if i == self.stop:
      raise StopIteration
    return i, e

def min(l):
  global _counter
  r = l[0]
  for pos, e in enumerate(l):
    _counter += 1
    if e < r:
      r = e
  return r, pos

def mysort1(l):
  for i,e in enum(l, stop=-1):
    print(i,l)
    m, off = min(l[i:])
    old = l[i]
    l[i] = m
    l[i+off] = old
  return l


def isort1(l):
  for i,e in enum(l, 1):
    i -= 1
    while (i >= 0) and (l[i] > e):
      l[i+1] = l[i]
      i -= 1
    l[i+1] = e
  return l


def isort2(l):
  for i,e in enum(l, 1):
    while (i > 0) and (l[i-1] > e):
      l[i] = l[i-1]
      i -= 1
    l[i] = e
  return l

def msort(l):
  """ merge sort"""
  size = len(l)
  if size == 1: return l
  left = msort(l[:size//2])
  right = msort(l[size//2:])
  r = []
  while left and right:
    if left[0] < right[0]:
      r.append(left.pop(0))
    else:
      r.append(right.pop(0))
  r += left + right
  return r


if __name__ == '__main__':
  l=[5,6,4,3,2,1]
  l=list(reversed(l))
  #print(mysort1(l))
  #print(isort1(l))
  print(msort(l))
