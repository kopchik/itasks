#!/usr/bin/env python3

def rhytm2(n=3, k=8):
  avg = k//n
  rem = k%n
  for i in range(n):
    print("!",end='')
    print("."*avg, end='')
  print("!"+"."*rem)


def rhytm(pn, an):
  ps = [[1] for _ in range(pn)]  # pulses
  ts = [[0] for _ in range(an-pn)]  # timings
  print(ps,ts)

  for x in range(3000):
    i = 0
    while ts and i<len(ps):
      t = ts.pop(0)
      ps[i] += t
      i += 1
    print("       ",ps, ts)
    if len(ts) == 1:
      break
    if not ts:
      ts = ps[i:]
      del ps[i:]
      print("shuffle", ps, ts)
  r = []
  for e in ps:
    r += e
  print("".join(map(str, r)))


if __name__ == '__main__':
  rhytm(3,8)
