#!/usr/bin/env python3

def getdeps(g, task):
  if task not in g:
    return [task]
  result = []
  for dep in g[task]:
    deps = getdeps(g, dep)
    for d in deps:
      if d not in result:
        result.append(d)
  return result


if __name__ == '__main__':
  g = {}
  g['A'] = ['B', 'C']
  g['B'] = "D E F".split()
  g['D'] = ['F']
  g['T'] = 'A B D'.split()
  print(getdeps(g, 'T'))
