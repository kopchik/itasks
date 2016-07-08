#!/usr/bin/env python3

def detect_cycle(g, head):
    visited = set()
    cur = head
    while True:
        visited.add(cur)
        cur = g[cur]
        if cur == -1:
          break
        elif cur in visited:
            print(1)
            return
    print(-1)

if __name__ == '__main__':
  l = [1, 2, -1]
  head = 0
  detect_cycle(l, head)
  
