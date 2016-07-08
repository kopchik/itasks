#!/usr/bin/env python3


my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

# destructive merge
def merge_lists(la, lb):
  result = []
  while la and lb:
    if la[0] < lb[0]:
      result.append(la.pop(0))
    else:
      result.append(lb.pop(0))
  result.extend(la or lb)
  return result


def merge_lists(la, lb):
  result = []
  ptra, ptrb= 0, 0
  while la[ptra:] and lb[ptrb:]:
    a = la[ptra]
    b = lb[ptrb]
    if a < b:
      result.append(a)
      ptra += 1
    else:
      result.append(b)
      ptrb += 1
  result.extend(la[ptra:] or lb[ptrb:])
  return result


print(merge_lists(my_list, alices_list))
