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

def max(l):
  global _counter
  r = l[0]
  for pos,e in enumerate(l):
    _counter += 1
    if e > r:
      r = e
  return r, pos

def mysort1(l):
  for i,e in enum(l, skip=1, stop=-1):
    m, pos = max(l[i:])
    old = l[i+pos]
    l[i] = m
    l[i+pos] = old
  return l


def isort(l):
  for i,e in enum(l, 1):
    print("sorting", e, "in", l)
    i -= 1
    while (i >= 0) and (l[i] > e):
      print("swaping %s and %s (i=%s)" % (l[i+1], l[i], i))
      l[i+1] = l[i]
      print("result:", l, i)
      i -= 1
    l[i+1] = e
    print(l)
  return l

if __name__ == '__main__':
  l=[6,5,4]
  #l=list(reversed(l))
  #print(mysort1(l))
  print(isort(l))
