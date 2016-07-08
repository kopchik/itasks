#!/usr/bin/env python3

M = 4
N = 4
calls = 0
def walk(x,y):
  global calls
  calls += 1
  if x >= M or y >= N:
    return
  if x == (M-1) and x == (N-1):
    yield 1
    return

  if  x < M -1:
    yield from walk(x+1, y)
  if  x < N -1:
    yield from walk(x, y+1)

print(sum(walk(0,0)))
print("calls", calls)
