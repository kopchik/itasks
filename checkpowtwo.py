#!/usr/bin/env python3


## replace with faster algo
def numbits(num):
  cnt = 0
  while num:
    cnt += num%2
    num = num>>1
  return cnt

def check(num):
  if num%2 or numbits(num) > 1:
    return False
  return True

if __name__ == '__main__':
  inpt = int(input("enter number: "))
  print(check(inpt))
