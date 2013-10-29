#!/usr/bin/env python3
from collections import defaultdict

class NoMatch(Exception): pass

def tuple_sum(a,s):
    global answer
    print(mysum(a,s))

answer = {}
def mysum(a, s, pos=0):
    global answer
    if s == 0: return []
    if not a: raise NoMatch

    best = None
    for i, e in enumerate(a[pos:], pos):
        print("trying {} on pos={}".format(i, pos))
        try:
          a = mysum(a, s-e, pos=i+1)
          print(a)
          if not best:
            best = a
          else:
            best = min(best, a)
        except NoMatch:
          pass
    return best

if __name__ == '__main__':
  a = list(map(int, "3 2 1 4 5 7 6 9 7 8".split()))
  tuple_sum(a, s=30)
