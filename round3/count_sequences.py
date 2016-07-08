#!/usr/bin/env python3

from collections import Counter

def validate(a):
  if not a:
    return 0
  c = Counter(a)
  return int(c['H'] >= c['T'])

def cut(a):
  if not a:
    yield []
    return
  for end in range(len(a)):
    head = a[:end+1]
    if not validate(head):
      continue
    tail = a[end+1:]
    for piece in cut(tail):
      yield [head] + piece


def count_sequences(data):
  for seq in cut(data):
    print(seq)

if __name__ == '__main__':
  data = [ 'H', 'T', 'H', 'T', 'T', 'H' ]
  #data = [ '1', '2', '3']
  count_sequences(data)
