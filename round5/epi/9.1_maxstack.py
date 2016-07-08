#!/usr/bin/env python3

def push(e, stack, track):
  stack.append(e)
  if not track:
    track.append(e)
    return
  if track[-1] <= e:
    track.append(e)


def pop(stack, track):
  e = stack.pop()
  if track[-1] == e:
    track.pop()
  return e

def getmax(stack, track):
  return track[-1]

if __name__ == '__main__':
  stack, track = [], []
  push(9, stack, track)
  print(getmax(stack, track))
  push(1, stack, track)
  print(getmax(stack, track))
  push(10, stack, track)
  print(getmax(stack, track))
  pop(stack, track)
  print(getmax(stack, track))
  
