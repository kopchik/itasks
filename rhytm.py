#!/usr/bin/env python3
from sys import stderr

def debug(*args, **kwargs):
  if __debug__:
    print(*args, file=stderr, **kwargs)


def goodtone(l):
  fst = l[0]
  for e in l[1:-1]:
    if e != fst:
      return False
  return True


def rhythm(pn, an):
  ps = [[1] for _ in range(pn)]  # pulses
  ts = [[0] for _ in range(an-pn)]  # timings
  debug("ps:", ps)
  debug("ts:", ts)

  while True:
    i = 0
    while ts and i<len(ps):
      t = ts.pop(0)
      ps[i] += t
      i += 1
    debug("       ",ps, ts)
    if len(ts) == 1 or \
       (ts == [] and goodtone(ps)):
        debug("good")
        break

    if not ts:
      ts = ps[i:]
      del ps[i:]
      debug("shuffle", ps, ts)

  # print result
  r = sum(ps+ts, [])
  print("".join(map(str, r)))


if __name__ == '__main__':
  rhythm(5,13)
  rhythm(3,8)

