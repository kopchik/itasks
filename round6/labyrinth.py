#!/usr/bin/env python
import math

N = 5

l = [['*' for x in range(N)] for x in range(N)]

def display(l):
  for row in l:
    print("".join(row))

def walk(l, n):
  center = math.floor(N/2)
  l[center][center] = '#'


walk(l, N)
display(l)
