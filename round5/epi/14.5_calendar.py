#!/usr/bin/env python3

def calMaxEvents(events):
  def key(ev):
    return ev[0]
  events.sort(key=key)
  hours  = [0 for _ in range(24)]

  for ev in events:
    start, stop = ev
    hours[start] += 1
    hours[stop]  -= 1

  maxcount = 0
  count = 0
  for i, stats in enumerate(hours):
    count += stats
    maxcount = max(maxcount, count)
    print("{:>10} {:>10}".format(i, count))
  print(maxcount)


if __name__ == '__main__':
  events = [
    (1,5),
    (6,10),
    (11,13),
    (14,15),
    (2,7),
    (8,9),
    (12,15),
    (4,5),
    (9,17),
    (4,10)
  ]
  calMaxEvents(events)
