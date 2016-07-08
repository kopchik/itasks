#!/usr/bin/env python3

def twonum(l, s):
  assert len(l) >= 2
  ptr1  = 0
  ptr2 = len(l) - 1
  csum = l[ptr1] + l[ptr2]
  while csum != s and ptr1<len(l) and ptr2 >= 0 and ptr1 != ptr2:
    print(ptr1, ptr2)
    csum = l[ptr1] + l[ptr2]
    if csum == s:
      return l[ptr1], l[ptr2]
    elif csum < s:
      ptr1 += 1
    elif csum > s:
      ptr2 -= 1
  raise Exception("No sum")

if __name__ == '__main__':
  print(twonum([1, 2, 4, 7, 11, 15], 15))
  
