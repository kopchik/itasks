#!/usr/bin/env python3

rawfile = open("largest-permutation-inpt.txt")
def input():
  return rawfile.readline()

N, K = input().split()
N, K = int(N), int(K)
numbers = list(map(int, input().split()))
pos = 0
perms = 0

myrange = range(1, N+1)
positions = {}
for i,e in enumerate(numbers):
  if e in myrange:
    positions[e] = i


for num in reversed(myrange):
  #idx = numbers.index(num)
  idx = positions[num]
  #print(num, idx, idx==pos)
  if idx != pos:
    other = numbers[pos]
    numbers[pos] = num
    numbers[idx] = other
    if other in myrange:
      positions[other] = idx
    perms += 1
    if perms == K:
      break
  pos += 1


print(" ".join(map(str,numbers)))
