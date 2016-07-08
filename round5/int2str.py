#!/usr/bin/env python3


def conv(num):
  digits = []
  negative = False
  if num < 0:
    num = -num
    negative = True
  while num > 0:
    digits.insert(0, num % 10)
    num //= 10
  if not digits:
    return "0"
  return ("-" if negative else "") + "".join(map(str, digits))


if __name__ == '__main__':
  print(conv(10))
  print(conv(-10))
  print(conv(0))

