#!/usr/bin/env python3

def groupby(l):
  grp = []
  r = [grp]
  elem = l[0]
  for e in l:
    if e == elem:
      grp.append(e)
    else:
      grp = [e]
      elem = e
      r.append(grp)
  return r


def ladder(l=[1]):
  print(l)
  new = l
  for x in range(5):
    old, new = new, []
    for grp in groupby(old):
      new.append(len(grp))
      new.append(grp[0])
    print(new)


if __name__ == '__main__':
  print(groupby([1,1,1,2,2,3]))
  ladder()

