#!/usr/bin/env python3

def rec(d=4):
  for i in range(-d,d+1):
    line = []
    for j in range(-d,d+1):
      v=(i*i+j*j)**0.5
      v = max(int(v)+1,int(v+1))
      line.append(v)
    print(line)

if __name__ == '__main__':
  rec()
  
