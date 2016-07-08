#!/usr/bin/env python3


def remove(l, e):
  ptr1 = 0
  ptr2 = len(l) - 1
  newlen = len(l)
  while ptr2 > ptr1:
    if l[ptr1] == e:
      newlen -= 1
      while l[ptr2] == e and ptr2 > ptr1:
        ptr2 -= 1
        newlen -= 1
      if ptr2 <= ptr1:
        break
      l[ptr1] = l[ptr2]
      ptr2 -= 1
    ptr1 += 1
  print(l[:newlen], newlen)


def remove2(l, e):
  ptr1 = 0
  ptr2 = len(l) - 1
  newlen = len(l)

  while ptr2 > ptr1:
    print(l)
    if l[ptr1] != e:
      ptr1 += 1
      continue
    l[ptr1] = l[ptr2]
    ptr2 -= 1
    newlen -= 1
  print(l[:newlen], newlen)


if __name__ == '__main__':
  test = [3, 2], 2
  print(remove(*test))
  
