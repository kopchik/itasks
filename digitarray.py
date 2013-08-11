#!/usr/bin/env python3

"""
Given a number represented as an array of digits, plus one to the number.
ie. 1000 is [1,0,0,0] result is [1,0,0,1]
"""

def digitize(num):
  seq = []
  while num:
    seq += [num%10]
    num = num//10
  return list(reversed(seq))

if __name__ == '__main__':
  print(digitize(int(input("Enter number: "))+1))
