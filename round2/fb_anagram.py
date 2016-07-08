#!/usr/bin/env python3

from collections import defaultdict


def store(array):
  result = defaultdict(list)
  for word in array:
    key = frozenset(word)
    result[key].append(word)
  return result

if __name__ == '__main__':
  array= ["tsar", "rat", "tar", "star", "tars", "cheese"]
  print(store(array))
