#!/usr/bin/env python3
import heapq


def walk(a, idx=0):
  left = 2*idx+1
  right = 2*idx+2
  if left < len(a):
    walk(a, left)
  if right < len(a):
    walk(a, right)
  print(a[idx])
if __name__ == '__main__':
  a = [4,3,2,1]
  a = [1,2,3,4]
  heapq.heapify(a)
  print(a)
  print(walk(a))
