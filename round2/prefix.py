#!/usr/bin/env python3
from collections import defaultdict

Dict = lambda: defaultdict(Dict)
root = Dict()

def check(d, word):
  if not word:
    return True
  if word[0] not in d:
    return False
  return check(d[word[0]], word[1:])


def insert(d, word):
  if not word:
    return
  return insert(d[word[0]], word[1:])


if __name__ == '__main__':
  insert(root, "test ")
  print(check(root, "test "))
  print(check(root, "nooo "))
