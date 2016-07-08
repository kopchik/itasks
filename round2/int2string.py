#!/usr/bin/env python3

def charmap(n):
  """ Returns char corresponding to digit. """
  assert 0 <= n <= 10
  return str(n)

def int2str(i):
  answer = []
  if i<0:
    i = -i
    answer.append('-')
  while True:
    answer.append(charmap(i%10))
    i //= 10
    if not i:
      break
  return "".join(answer)

assert int2str(1) == "1"
assert int2str(666) == "666"
assert int2str(0) == "0"
assert int2str(-1) == "-1"

