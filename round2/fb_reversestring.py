#!/usr/bin/env python3

def reverse(l):
  for i in range(len(l)//2):
    j = len(l) - i - 1
    l[i], l[j] = l[j], l[i]
  return l

if __name__ == '__main__':
  print(reverse(list("test")))
  print(reverse(list("54321")))
  
