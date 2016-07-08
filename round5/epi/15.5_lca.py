#!/usr/bin/env python3

def walk(node, a, b):
  while True:
    value = node.value
    if value == a or value == b or (a < value < b):
      return node

    if max(a,b) < value:
      node = node.left
    else:
      node = node.right
    return node
