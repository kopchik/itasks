#!/usr/bin/env python3
# find lowest current ancestor LCA
from collections import namedtuple
Node = namedtuple('Node', ['value', 'children'])

def find(g, elem, path=()):
  value, children = g
  path = path + (value,)
  if value == elem:
    return path
  for child in children:
    try:
      return find(child, elem, path)
    except KeyError:
      pass
  raise KeyError


def _lca(path1, path2):
  result = path1[0]
  for i, (e1,e2) in enumerate(zip(path1, path2)):
    if e1 != e2:
      break
    result = e1
  return result


def lca(g, elem1, elem2):
  return _lca(find(g, elem1),
              find(g, elem2))

def lca2(g, e1, e2):
  value, children  = g
  if value in [e1, e2]:
    return value
  if e1 < value and e2 < value:
    return lca2(children[0], e1, e2)
  if e1 >= value and e2 >= value:
    return lca2(children[1], e1, e2)
  else:
    return value


def walk(queue):
  for node in queue:
    value, children = node
    print(value)
    queue.extend(children)


def walk2(g):
  value, children = g
  for child in children:
    walk2(child)
  print(value)

if __name__ == '__main__':
  graph = Node(1,
            [Node(2,[]),
            Node(3,
              [Node(4,[])
            ])
          ])
  #assert lca2(graph, 1, 1) == lca(graph, 1, 1) 
  #walk([graph])
  walk2(graph)
