#!/usr/bin/env python3
"""
Given a BST, maximum and minimum value, find the sum of nodes with values between the above range
"""

from ds import BPNode


def findtop(n):
  """ find root of tree """
  if not n.parent:
    return n
  return findtop(n.parent)


def find(n, v):
  if n is None:
    return None
  if n.value == v:
    return n
  return find(n.left, v) or find(n.right, v)


def findup(n, v, prev=None):
  if n.value == v:
    return n
    return find(n.left,v)
    if r: return r

  return (n.left != prev  and find(n.left, v))  \
      or (n.right != prev and find(n.right, v)) \
      or findup(n.parent, v, prev=n)


if __name__ == '__main__':
  l = [1,2,3,4,5,6]
  root = BPNode.from_list(l)
  print(root)
  node = root.left.right
  top = findtop(node)
  print(find(top, 3))
  print(findup(node, 3))
