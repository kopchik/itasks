#!/usr/bin/env python3

def min_battery(l):
  assert len(l) > 2
  battery = 0
  min_battery = 0
  cur = l[0]
  for i, nxt in enumerate(l[1:], 1):
    battery += (nxt - cur)
    min_battery = max(battery, min_battery)
    cur = nxt
  return min_battery

if __name__ == '__main__':
  print(min_battery([1,2,3,4,0]))
