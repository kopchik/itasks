#!/usr/bin/env python3

import sys
sys.setrecursionlimit(10)

def match(string, pattern, spos=0, ppos=0):
  print(string, pattern, spos, ppos)
  while ppos < len(pattern):
    p = pattern[ppos]
    if spos ==len(string) and p != '$':
        print("we reached the end of the string, no match")
        return False


    print("matching", string[spos:], "with", pattern[ppos:], "pos", spos)
    if p == '^':
      if spos != 0:
        return False
      # spos += 1
    elif p == '$':
      if spos != len(string):
        return False
      spos += 1
    elif p == '.':
      spos += 1
    elif p == '*':
      if spos + 1 == len(string):
        return True
      for newpos in range(spos+1, len(string)):
        if match(string, pattern, newpos, ppos+1):
          return True
      return False
    else:
      print("> regular matching", p, string[spos])
      if p != string[spos]:
        return False
      spos += 1

    ppos += 1

  return True



if __name__ == '__main__':
  tests = [
    ('a', '*', True),
    ('aa', '*', True),
    ('aa', '*', True),
    ('aa', '*$', True),
    ('aa', 'a*$', True),
    ('haba', '*ba', True),
    ('haba', '*ba', True),
    ('haba', 'haba$', True),
    ('haba', '^haba$', True),
    ("haba", "*aba", True),
    ("haba", ".aba", True),
    ("haba", "h*a", True),
    ("haba", "h*ba", True),
    ("haba", "^$", False),
    ]

  for string, pattern, result in tests:
    if match(string, pattern) != result:
      print("! mismatch on", string, pattern)