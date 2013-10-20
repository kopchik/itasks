#!/usr/bin/env python3
class Q:
  def __init__(self, maxlen=3):
    self.list = [None for _ in range(maxlen)]
    self.head = maxlen -1 
    self.tail = 0
    self.len  = 0
    self.maxlen = maxlen

  def add(self, e):
    if self.len == self.maxlen:
      raise Exception("Queue is full")
    self.len += 1
    self.tail -= 1
    self.tail %= self.maxlen
    self.list[self.tail] = e

  def getlen(self):
      return self.len

  def rem(self):
    if self.len == 0:
      raise Exception("Queue is empty")
    e = self.list[self.head]
    self.head -= 1
    self.head %= self.maxlen
    self.len -= 1
    return e

  def __repr__(self):
    answer = []
    ptr = self.tail
    for i in range(self.len):
      answer.append(self.list[ptr])
      ptr += 1
      ptr %= self.maxlen
    return "%s (%s h:%s t:%s)" % (answer, self.list, self.head, self.tail)
q=Q()
print(q)
q.add(1)
q.add(2)
print(q)
while q.getlen():
  print("got", q.rem())
print(q)
q.add(1)
q.add(2)
q.add(3)
print(q)
while q.getlen():
  print("got", q.rem())
print(q)
q.add(1)
q.rem()
print(q)
q.add(1)
q.rem()
print(q)
