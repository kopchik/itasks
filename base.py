#!/usr/bin/env python3

alphabet="0123456789ABCDEF"

map_ = {v:s for v,s in enumerate(alphabet)}
def conv(v, base=3):
  r = ""
  while v >= base:
    r += map_[v%base]
    v //= base
  r += map_[v]
  return list(reversed(r))

print(conv(571,base=8))
