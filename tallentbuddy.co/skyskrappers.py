#!/usr/bin/env python3

def getrmaxes(hs):
  i = len(hs)-1
  maxright = hs[i]
  tbl = [0]*len(hs)
  while i:
    maxright = max(maxright, hs[i])
    tbl[i] = maxright
    i -= 1
  return tbl

def skyscrapers(hs):
  num = len(hs)
  i = 1
  volume = 0
  lmax = 0
  tbl = getrmaxes(hs)
  rmax = tbl[0]
  #print(hs)
  while i < len(hs)-1:
    prev, cur, nxt = hs[i-1:i+2]
    lmax = max(lmax, prev)
    rmax = tbl[i]
    #print(prev, cur, nxt)
    #print(lmax, rmax)
    v = min(lmax,rmax)-cur
    if v > 0: volume += v
    i += 1
  print(volume)


if __name__ == '__main__':
  #heights = [9, 8, 7, 8, 9, 5, 6]
  heights = [1,9,7,6,6,7,8,3,3,3,5,1]
  #from inpt import heights
  #print(len(heights), min(heights), max(heights))
  #exit()
  skyscrapers(heights)
