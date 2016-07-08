#!/usr/bin/env python3

#find majority element

def find_majority_elem(stream):
  candidate = None
  count = 0
  for w in stream:
    if w == candidate:
      count +=1
      continue
    else:
      if count == 0:
        count = 1
        candidate = w
      else:
        count -= 1
  return candidate


if __name__ == '__main__':
  test = "1 2 1 2 2".split()
  print(find_majority_elem(test))
