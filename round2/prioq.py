#!/usr/bin/env python3

class Node:
  value = None
  left = None
  right = None
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

  def put(self, node):
    if node.value <= self.value:
      if not self.left or node.value >= self.left.value:
        node.left = self.left
        self.left = node
      else:
        self.left.put(node)
    elif node.value > self.value:
      if not self.right or node.value <= self.right.value:
        node.right = self.right
        self.right = node
      else:
        self.right.put(node)

  def getmax(self, parent=None):
    if self.right:
      return self.right.getmax(self)
    if parent:
      parent.right = None
    return self.value

  def __repr__(self):
    return "({} {} {})".format(self.value, self.left, self.right)


root = Node(0)
print(root)
root.put(Node(1))
print(root)
root.put(Node(3))
root.put(Node(10))
root.put(Node(9))

while True:
  value = root.getmax()
  print(value, root)
  if not value:
    break
