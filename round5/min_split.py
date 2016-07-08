#!/usr/bin/env python3

def is_pali(s):
  assert s
  if len(s) == 1:
    return True
  for idx in range(len(s)//2):
    if s[idx] != s[len(s)-idx-1]:
      return False
  return True


# TODO: cache
minsplits = {}
def splits(s):
  if not s:
    return 0
  if len(s) == 1:
    return 0
  min_splits = 99999
  for pos in range(1, len(s)):
    print("trying", s[:pos])
    if is_pali(s[:pos]):
      num_splits = 1 + splits(s[pos:])
      if num_splits < min_splits:
        min_splits = num_splits
  if min_splits == 99999:
    print("!", s)
  print(s, min_splits)
  return min_splits

if __name__ == '__main__':
  print(splits("abbab"))

