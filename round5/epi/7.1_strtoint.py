#!/usr/bin/env python3

def itoa(num):
  numbers = []
  while num:
    numbers.insert(0, str(num % 10))
    num //= 10
  return "".join(numbers)


def atoi(s):
  num = 0
  for i, lit in enumerate(s):
    num = num*10 + (ord(lit) - ord('0'))
  return num


if __name__ == '__main__':
  print(itoa(359))
  print(atoi("359"))
  
