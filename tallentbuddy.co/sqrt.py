#!/usr/bin/env python3

def compute_sqrt(n):
    upper=n//2
    lower=0
    candidate = n//4
    while abs(upper-lower)>1:
        if candidate**2 > n:
            upper = candidate
        else:
            lower = candidate
        candidate = (upper+lower)//2
    print(lower)

if __name__ == '__main__':
  compute_sqrt(18)
