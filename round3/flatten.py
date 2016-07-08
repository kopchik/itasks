#!/usr/bin/env python3

def flatten(l):
  for e in l:
    if isinstance(e, (list, tuple)):
      yield from flatten(e)
    else:
      yield e

if __name__ == '__main__':
  data = [[[1]],[], 2]
  print(list(flatten(data)))
  
