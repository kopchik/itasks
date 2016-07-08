#!/usr/bin/env python3
def gen(array, N, ind):
  a = 1
  while a <= N:
    k = ind % a
    ind //= a
    array[a-1] = array[k]
    array[k] = a
    a += 1

if __name__ == '__main__':
  a = [1,2,3]
  #for i,_ in enumerate(a):
  for N in range(1,4):
    for i in range(3):
      gen(a, N, i)
    print(a)
  
