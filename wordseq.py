#!/usr/bin/env python3
"""
Given a source string and a destination string write a program to display sequence of strings to travel from source to destination. Rules for traversing:
1. You can only change one character at a time
2. Any resulting word has to be a valid word from dictionary
Example: Given source word CAT and destination word DOG , one of the valid sequence would be
CAT -> COT -> DOT -> DOG
Another valid sequence can be
CAT -> COT - > COG -> DOG

One character can change at one time and every resulting word has be a valid word from dictionary
"""
## time: ~40mins

words = "cat cot cog dot dog".split()

def dist(word1, word2):
  if len(word1) != len(word2):
    return -1
  diff = 0
  for c1, c2 in zip(word1, word2):
    if c1 != c2:
      diff += 1
  return diff


def _traverse(src, dst, path=[], words=words):
  if src == dst:
    return [path]

  results = []
  for w in words:
    if dist(src, w) == 1 and (w not in path):
      results += _traverse(w, dst, path+[w], words)
  return results


def traverse(src, dst, words=words):
  return _traverse(src, dst, path=[src], words=words)


if __name__ == '__main__':
  print(traverse("cat", "dog") or "No way :)")
