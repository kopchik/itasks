#!/usr/bin/env python3
from enum import Enum
from useful.infix import infix_decorator
import nose

LESS    = object()
EQUAL   = object()
MORE    = object()
BEFORE  = object()
OVERLAP = object()
AFTER   = object()


left = 0
right = 1
def overlaps(a,b):
  if a[left] > b[right] or b[left] > a[right]:
    return False
  return True

def includes(a,b):
  if a[left] <= b[left] and a[right] >= b[right]:
    return True
  return False


@infix_decorator
def cmp(a, b):
  if a == b: return EQUAL
  if includes(a,b): return MORE
  if includes(b,a): return LESS
  if overlaps(a,b): return OVERLAP
  if a[left] < b[right]: return BEFORE
  return AFTER


class Node:
  def __init__(self, value):
    self.value = value
    self.children = {}
  def insert(self, value):
    if self.value == value:
      return
    cmp_res = cmp(self.value, value)
    if cmp_res in  self.children:
      child = self.children[cmp_res]
      return child.insert(value)
    else:
      self.children[cmp_res] = value
      return

  def find(self, value):
    cmp_res = cmp(self.value, value)
    if cmp_res not in
if __name__ == '__main__':
  assert cmp((1,1), (1,1)) == EQUAL
  assert cmp((1,1), (1,2)) == LESS
  assert cmp((1,2), (1,1)) == MORE
  assert cmp((1,9), (2,3)) == MORE
  assert cmp((1,2), (3,4)) == BEFORE
  assert cmp((7,8), (5,6)) == AFTER

  root = Node((1,10))
  root.insert((1,20))
  root.insert((3,9))
  
