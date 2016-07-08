#!/usr/bin/env python3

k=6
l=range(20)
runner1 = iter(l)
runner2 = iter(l)
[next(runner2) for i in range(k)]
while True:
  try:
    v=next(runner1)
    next(runner2)
  except StopIteration:
    print(v)
    break
