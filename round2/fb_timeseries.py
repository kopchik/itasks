#!/usr/bin/env python3
#Given two unsorted arrays, one with event start times and one with end times, find out if any two events overlap.

from collections import namedtuple

TSBase = namedtuple('TS', ['start', 'end'])


class TS(TSBase):
  def overlap(self, other):
    return    self.end < other.start  \
           or self.start < other.end

if __name__ == '__main__':
  a1 = [0,1,2,3]
  a2 = [3,4,5,2]
  series = [TS(start, end)
              for start, end in zip(a1,a2)]
  for i,ts1 in enumerate(series[:-1]):
    for ts2 in series[i+1:]:
      if ts1.overlap(ts2):
        print("overlaps:", ts1, ts2)
