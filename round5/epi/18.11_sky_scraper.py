#!/usr/bin/env python3

def get_max_left(a):
  max_e = -1
  max_e_pos = -1
  ret = []
  positions = []
  for pos, e in reversed(list(enumerate(a))):
    if e >= max_e:
      max_e = e
      max_e_pos = pos
    ret.insert(0, max_e)
    positions.insert(0, max_e_pos)
  return ret, positions

def max_trapped(a):
  max_left, max_left_pos = get_max_left(a)
  print(max_left, max_left_pos)
  maxvol = -1
  ret = None
  for pos, e in enumerate(a):
    level = min(e, max_left[pos])
    volume = (max_left_pos[pos] - pos) * level
    if volume > maxvol:
      print("candidate", pos, max_left_pos[pos])
      ret = pos, max_left_pos[pos]
  return ret

if __name__ == '__main__':
  heights = [2,0,1]
  print(max_trapped(heights))
  
