#!/usr/bin/env python3

def check(n):
  orig = n
  while n:
    digit = n % 10
    if digit not in [0,1]:
      return False
    n //= 10
  return orig


def number(n, i=1):
  candidate = n*i
  return check(candidate) or number(n, i+1)


def number2(n, candidate=1):
  candidate *= 10
  if not n % candidate:
    return candidate
  candidate += 1
  if not n % candidate:
    return candidate
  return number2(n, cand)


def bin2dec(n):
  numbers = []
  while n:
    numbers.append(n%2)
    n //= 2
  return sum(10**i*n for i, n in enumerate(numbers))


def number2(n=1):
  i = 1
  while True:
    candidate = bin2dec(i)
    if not candidate % n:
      return candidate
    i += 1



if __name__ == '__main__' or 1:
  assert number2(4) == 100
