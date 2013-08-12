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


class BNode:
  """ BTree
  """
  value = None
  left = None
  right = None
  @classmethod
  def from_list(cls, l):
    if not l:
      return None
    root = BNode()
    left, value, right = brk(l)
    root.value = value
    root.left = BNode.from_list(left)
    root.right = BNode.from_list(right)
    return root

  def __str__(self):
    name = self.__class__.__name__
    return "{}({} {} {})".format(name, self.value, self.left, self.right)


class BPNode:
  """ BTree with links to the parent nodes
  """
  value = None
  left = None
  right = None
  parent = None
  @classmethod
  def from_list(cls, l, parent=None):
    if not l:
      return None
    root = BPNode()
    root.parent = parent
    left, value, right = brk(l)
    root.value = value
    root.left = BPNode.from_list(left, parent=root)
    root.right = BPNode.from_list(right, parent=root)
    return root

  def __str__(self):
    name = self.__class__.__name__
    return "{}({} {} {})".format(name, self.value, self.left, self.right)
