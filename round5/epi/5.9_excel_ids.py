#!/usr/bin/env python3

def to_int(s):
  return sum((ord(c) - ord('A') + 1)*(26**pos) for pos,c in enumerate(reversed(s)))


if __name__ == '__main__':
  test = "A B Z AA AB ZZ".split()
  print([(id, to_int(id)) for id in test])
