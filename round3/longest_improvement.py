#!/usr/bin/env python3

def longest_improvement(grades):
  longest = 0
  cnt = 1
  for x1, x2 in zip(grades, grades[1:]):
    if x1 <= x2:
      cnt += 1
    else:
      longest = max(longest, cnt)
      cnt = 1
  print(max(longest, cnt))


if __name__ == '__main__':
  inpt = [9, 7, 8, 2, 5, 5, 8, 7]
  assert longest_improvement(inpt) == 4

