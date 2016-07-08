#!/usr/bin/env python3


def bipartite(tree, root):
  """ TODO: some docstring. """
  colors  = {}
  queue = [(root, True)]
  while queue:
    node, color = queue.pop(0)
    if node in colors:
      if colors[node] != color:
        return False
    else:
      colors[node] = color
      for adj in tree[node]:
        queue.append((adj, not color))
  return True

if __name__ == '__main__':
  tree = {}
  #tree[1] = [2,3]
  #tree[2] = [1,3]
  #tree[3] = [1,2]
  tree[1] = [1,2]
  tree[2] = [1]
  print(bipartite(tree, 1))
