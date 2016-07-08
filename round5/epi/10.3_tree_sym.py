#!/usr/bin/env python3
from operator import eq

direct = lambda l: l

def traverse(tree, f=direct):
  #print('traversing', tree)
  if not tree:
    return
  #print("*", tree, list(f(tree)))
  for val, subtree in f(tree):
    #print("yielding", val, subtree)
    yield(val)
    #assert isinstance(subtree, list)
    yield from traverse(subtree, f)

 

myeq = lambda l: eq(l[0], l[1])
if __name__ == '__main__':
  tree = [(1,
          [(3,[]), (3,[])])
         ]
  t1 = traverse(tree)
  t2 = traverse(tree, reversed)
  print(all(e1 == e2 for e1,e2 in zip(t1,t2)))
  print(all(map(myeq, zip(t1,t2))))
