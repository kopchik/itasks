#!/usr/bin/env python3

def rev(s):
  s = list(s)
  l = len(s)
  for i in range(l//2):
    s[i], s[l-i-1] = s[l-i-1], s[i]

  start, stop = 0, 0
  ptr = 0
  s += [' ']
  for i, (cur, nxt) in enumerate(zip(s[:-1], s[1:])):
    if cur.isspace() and not nxt.isspace():
      start = i+1
      print("start", start)
    if not cur.isspace() and nxt.isspace():
      stop = i
      print("stop", stop)
      print(s[start:stop+1])
      for ptr in range(start, stop):
        if ptr > (start+stop) // 2:
          break
        s[ptr], s[start+stop-ptr] = s[start+stop-ptr], s[ptr]
        print(s)
  return "".join(s)



if __name__ == '__main__':
  test = ["Alice likes Bob"]
  for t in test:
    print(t, '===', rev(t))
