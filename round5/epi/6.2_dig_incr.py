#!/usr/bin/env python3

def to_digits(n):
  if not n: return [0]
  digits = []
  while n:
    digits.insert(0, n%10)
    n //=10
  return digits


# achtung! modifies argument!
def inc(digits):
  for i, d in reversed(list(enumerate(digits))):
    d = (d +1) % 10
    digits[i] = d
    if d: break
  else:
    digits.insert(0, 1)
  return digits


if __name__ == '__main__':
  test = [ 10, 99, 0]
  for t in test:
    digits = to_digits(t)
    print(digits, end=' ')
    inc(digits)
    print(digits)
