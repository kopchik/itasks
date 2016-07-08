#!/usr/bin/env python3

# 1: check if they have nodes in common -- we can traverse both lists in full.
# if we end up in the same place (the last node) we know they have some last nodes in common.

l1 = [1,2,3,4,6,7,8,9]
l2 = [11,12,13,7,8,9]

def get_last_node(l):
  for x in l:
    pass
  return (x, len(l))

if __name__ == '__main__':
  last_l1, len_l1 = get_last_node(l1)
  last_l2, len_l2 = get_last_node(l2)
  print(last_l1 == last_l2, len_l1-abs(len_l2 - len_l1) + 1)
