#!/usr/bin/env python3


def check(s):
  l = len(s)
  for i in range(l//2):
    if s[i] != s[l-i-1]:
      return False
  return True

if __name__ == '__main__':
  test = ["haba", '111', '1231231', '123321', '12321', '', '1']
  for t in test:
    print(check(t), t)
  
