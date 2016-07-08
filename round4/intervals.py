#!/usr/bin/env python3

def merge(disjoint, join):
  curl, curr = join
  printed = False
  for l,r in disjoint:
    if r < curl:
      print((l,r))
      continue
    elif l > curr:
      print((curl, curr))
      printed = True
      print((l,r))
    else:
      curl = min(l,r, curr, curl)
      curr = max(l,r, curr, curl)
  if not printed:
    print((curl, curr))


if __name__ == '__main__':
  inpt = ([(1, 5), (10, 15), (20, 25)], (12, 27))
  merge(*inpt)
  #Out: [(1, 5), (10, 27)]

# (1, 5), (10, 15), (20, 25),
#            (12,              27)

