#!/usr/bin/env python3

def rhytm2(n=3, k=8):
  avg = k//n
  rem = k%n
  for i in range(n):
    print("!",end='')
    print("."*avg, end='')
  print("!"+"."*rem)


def rhytm(n, k):
  bins1 = [[1] for _ in range(n)]
  bins2 = [[0] for _ in range(k)]

  for x in range(3000):
    i = 0
    while bins2 and i<len(bins1):
      b2 = bins2.pop(0)
      bins1[i] += b2
      i += 1
    if len(bins2) in [0,1]:
      break
    if not bins2:
      bins2 = bins1[i:]
      del bins1[i:]
  print(bins1, bins2)
  r = []
  for elem in bins1:
    r += elem
  print("".join(map(str, r)))


if __name__ == '__main__':
  rhytm(3,8)
