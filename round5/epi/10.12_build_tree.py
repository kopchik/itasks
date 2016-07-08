#!/usr/bin/env python3

from collections import defaultdict
from pprint import pprint

def getroot():
  return defaultdict(getroot)
root = getroot()


def build(tree, inorder, preorder):
  if not inorder or not preorder:
    return tree
  value = preorder.pop(0)
  tree['value'] = value
  pos = inorder.index(value)
  left, right = inorder[:pos], inorder[pos+1:]
  print('======')
  print('left',left)
  print('right', right)
  print('preorder', preorder)
  build(tree['left'],  left,  preorder)
  build(tree['right'], right, preorder)
  return tree

if __name__ == '__main__':
  preorder =  'H B F E A C D G I'.split()
  inorder =   'F B A E H C D I G'.split()
  pprint(build(root, inorder, preorder))
