#!/usr/bin/env python3

def traverse(node, f):
  for i, e in enumerate(node):
    r = f(e)
    if isinstance(r, list):
      traverse(r, f)
    node[i] = r
    

if __name__ == '__main__':
  tree = [1,4,[3]]
  def f(node):
    if node == 4:
      node = 9999
    return node
  print(tree)
  traverse(tree, f)
  print(tree)
  
