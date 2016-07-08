#!/usr/bin/env python3

def count(s):
  lastc = s[0]
  cnt = 1
  for c in s[1:]:
    if c == lastc:
       cnt += 1
    else:
       cnt -= 1
    if cnt <= 0:
      lastc = c
      cnt = 1
  return lastc

if __name__ == '__main__':
  data = "0010112"
  print(count(data))
  
