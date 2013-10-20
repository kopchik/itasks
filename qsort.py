#!/usr/bin/env python3
from random import randint

def split(arr, e):
  l = []
  r = []
  es = []
  for x in arr:
    if x<e:
      l.append(x)
    elif x>e:
      r.append(x)
    else:
      es.append(x)
  return l, es, r

def qsort(arr):
  if not arr:
    return arr
  l, p, r = split(arr, arr[0])
  return qsort(l) + p + qsort(r)

class Num:
  cnt = 0
  def __init__(self, num):
    self.num = num
    self.cnt = Num.cnt
    Num.cnt += 1
  def __eq__(self, other):
    return self.num == other.num
  def __lt__(self, other):
    return self.num < other.num
  def __repr__(self):
    return "(%s, %s)" % (self.num, self.cnt)

def partition(A, left, right, pivotIndex):
  pivotValue = A[pivotIndex]
  A[pivotIndex], A[right] = A[right], A[pivotIndex]
  storeIndex = left
  for i in range(left, right):
    if A[i] <= pivotValue:
      A[i], A[storeIndex] = A[storeIndex], A[i]
      print(A, i, storeIndex)
      storeIndex += 1
  A[right], A[storeIndex] = A[storeIndex], A[right]
  print()
  print(A)
  return storeIndex
#d = [0, 1, 9, 3, 5, 4]
d = [Num(randint(0,10)) for _ in range(10)]
#print(qsort(d))
partition([1,2,3,4,5,6], 0, 5, 2)
