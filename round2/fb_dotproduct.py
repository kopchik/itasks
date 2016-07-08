#!/usr/bin/env python3

def product(v1, v2):
  return sum(e1*e2 for e1,e2 in zip(v1,v2))

if __name__ == '__main__':
  print(product((3,-2,6), (2,3,-5)))
