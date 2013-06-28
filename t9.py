#!/usr/bin/env python3
# Time: about 30 minutes
# Idea: we build a B-tree
from functools import reduce
from collections import defaultdict as ddict

mapping = [(2, "abc"), (3, "def"), (4, "ghi"),
           (5, "jkl"), (6, "mno"), (7, "pqrst"),
           (8, "tuv"), (9, "wxyz")]

dictionary = ["abc", "test", "haba", "foo", "bar"]

kbdmap = {}
for k, chars in mapping:
  for c in chars: kbdmap[c] = k

def word2seq(word):
  return reduce(lambda seq, c: seq+[kbdmap[c]], word, [])


class Node:
  ''' A basic build block of a tree.
      No method modifies it's argument.
  '''
  def __init__(self):
    self.children = {}
    self.words = []

  def addword(self, word):
    path = word2seq(word)
    self.add(path, word)

  def add(self, path, word):
    if not path:
      if word not in self.words:
        self.words += [word]
      return
    elem = path[0]
    if elem not in self.children:
      leaf = Node()
      self.children[elem] = leaf
    else:
      leaf = self.children[elem]
    leaf.add(path[1:], word)

  def suggest(self, path):
    return self.subtree(path).traverse()

  def subtree(self, path=[]):
    if not path:
      return self
    elem = path[0]
    if elem not in self.children:
      raise Exception("No such path")
    tree = self.children[elem]
    return tree.subtree(path[1:])

  def traverse(self):
    result = []
    for tree in self.children.values():
      result += tree.traverse()
    return self.words + result


if __name__ == '__main__':
  root = Node()
  for word in dictionary:
    root.addword(word)
  #list(map(lambda w: root.addword(w), dictionary))
  print("for 222:", root.suggest([2,2,2]))
