#!/usr/bin/env python3

class Node:
  def __init__(self, value, next=None):
    self.value=value
    self.next = next
  def __repr__(self):
    return "(%s, %s)" % (self.value, self.next)

def get_list(l):
  cur = Node(l[0])
  head = cur
  for e in l[1:]:
    nxt = Node(e)
    cur.next = nxt
    cur = nxt
  return head

def merge(a, b):
  if a.value < b.value:
    cur = a
    a = a.next
  else:
    cur = b
    b = b.next
  head = cur
  while a and b:
    print(head, '\n', cur, a, b)
    print()
    if a.value < b.value:
      cur.next = a
      a = a.next
      cur = a
    else:
      cur.next = b
      b = b.next
      cur = b

  if a:
    cur.next = a
  else:
    cur.next = b
  return head

if __name__ == '__main__':
  print(merge(get_list([1,3,5]), get_list([2,4])))
  
