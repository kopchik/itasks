#!/usr/bin/env python3


def split(m,n,k):
  #if m%(k+1) == 0:
  #  return n*(m//(k+1))
  #if n%(k+1) == 0:
  #  return m*(n//(k+1))
  if k <= min(m,n):
    return (m*n)//(max(m,n)//(k+1))
  else:
    k2 = k - (min(m,n) - 1)
    return max(m,n) // k2

def test_split():
  assert split(4,1,1) == 2
  assert split(4,2,1) == 4
  assert split(4,2,3) == 2
  assert split(5,2,3) == 2
  
