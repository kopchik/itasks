#!/usr/bin/env python3
# merge timeseries together
from collections import namedtuple

class TS(namedtuple('TSBase', ['start', 'end'])):
  def overlaps(self, other):
    return not (self.end < other.start or self.start > other.end)

  def merge(self, other):
    assert self.overlaps(other),  \
        "not overlapping: {} and {}".format(self, other)
    return TS(min(self.start, other.start),
              max(self.end, other.end))


series = [TS(0,1), TS(0, 1)] #, TS(3,4), TS(1,2), TS(2,3)]

if __name__ == '__main__':
  print(TS(1,3).overlaps(TS(-1,1)))
  series.sort()
  result = []
  ts1 = series[0]
  for ts2 in series[1:]:
    if ts1.end >= ts2.start:
      ts1 = ts1.merge(ts2)
    else:
      result.append(ts1)
      ts1 = ts2
  result.append(ts1)
  print(result)



