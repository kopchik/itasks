#!/usr/bin/env python3
"""
Given a BST, maximum and minimum value, find the sum of nodes with values between the above range
"""

def brk(l):
  assert(l), "cannot brake empty list"
  l    = sorted(l)
  mid  = len(l)//2
  less = l[:mid]
  more = l[mid:]
  if less:
    pivot = less.pop()
  else:
    pivot = more.pop()
  return less, pivot, more


class Node:
  value = None
  left = None
  right = None
  @classmethod
  def from_list(cls, l):
    if not l:
      return None
    root = Node()
    left, value, right = brk(l)
    root.value = value
    root.left = Node.from_list(left)
    root.right = Node.from_list(right)
    return root

  def __str__(self):
    return "({} {} {})".format(self.value, self.left, self.right)


def traverse(root, r):
  if not root: return 0

  if root.value in r:
    return root.value + traverse(root.left, r) + traverse(root.right, r)
  elif root.value < r.start:
    return traverse(root.right, r)
  else:
    return traverse(root.left, r)

if __name__ == '__main__':
  l = [1,2,3,4,5,6]
  root = Node.from_list(l)
  print(root)
  print(traverse(root, range(3,5)))
