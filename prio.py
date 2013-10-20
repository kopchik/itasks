#!/usr/bin/env python3
from useful.mstring import s
# http://www.talentbuddy.co/challenge/51ce446a4af0110af3826346

def myrange(stop): return range(stop+1)
def count(a,b,c, cap):
  result = 0
  for i in myrange(a):
    for j in myrange(b):
      for k in myrange(c):
        if i+j+k == cap:
          result += 1
  return result

def count_configurations(a, b, c, n):
    # Write your code here.
    x = a+b+c
    y = subset(x, n)
    print(y - b + 1 - c + 1 - a*b - a*c + b + c -c + 1 - b*c + c)

def subset(n, k):
    if k == 0:
        return 1
    if n == k:
        return 1
    else:
        return subset(n-1, k-1) + subset(n-1, k)

print(count_configurations(1, 1, 1, 2))
print(subset(4,2))
#print( count([2,2,2],3))
#print( count(2,2,2,2))
