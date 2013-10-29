#!/usr/bin/env python3

def lmaxpop(l):
    """ let's assume it has NlogN complexity :)
    """
    l.remove(max(l))

def select_numbers(v, k):
    lmax = 0;
    l = []
    for e in v:
        if e < lmax:
            if len(l) >= k:
              lmaxpop(l)
            l.append(e)
            lmax = max(l)
        elif e > lmax:
            if len(l) < k:
                lmax = e
                l.append(e)
    print(" ".join(map(str,l)))

if __name__ == '__main__':
  v = [54553,201557,858524,95183,665451,314047,875607,596111,952362]
  k = 3
  print(select_numbers(v,k))
