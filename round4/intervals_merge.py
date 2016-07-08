#!/usr/bin/env python3
from useful.mstring import prints

left = 0
right = 1
def includes(a,b):
  if a[left] <= b[left] and a[right] >= b[right]:
    return True
  return False


def overlaps(a,b):
  if a[left] > b[right] or b[left] > a[right]:
    return False
  return True


def merge2(a,b):
  return (min(a+b), max(a+b))


def merge(inpt):
  inpt = sorted(inpt)
  result = []

  a = inpt[0]
  for b in inpt[1:]:
    if overlaps(a,b):
      a = merge2(a,b)
    else:
      result.append(a)
      a = b
  else:
    result.append(a)

  return result


if __name__ == '__main__':
  inpt=[(1,2), (3,4), (1,8), (15,16), (16,17)]
  print(merge(inpt))
