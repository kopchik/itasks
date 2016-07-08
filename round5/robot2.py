#!/usr/bin/env python3


def robot(M,N):
  prev = [1 for x in range(M)]
  next = [0 for x in range(M)]
  for pos in range(1,len(prev)):
    prev[pos] = 1
  for _ in range(N):
    print(prev)
    for pos in range(M):
      prev[pos]
      next[pos] = prev[pos]
      if pos > 0:
        next[pos] += next[pos-1]
    prev, next = next, prev
  return next[-1]


from math import factorial
def robot_fac(M, N):
  return factorial(M+N-2)/ (factorial(M-1)*factorial(N-1))

if __name__ == '__main__':
  print(robot(3, 3), robot_fac(3,3))

