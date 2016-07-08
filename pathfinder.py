#!/usr/bin/env python3

labirinth = [
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
]
class PTR:
  def __init__(self, x, y):
    self.x, self.y = x, y
  def __add__(self, other):
    return PTR(self.x + other.x, self.y + other.y)
  def __eq__(self, other):
    return (self.x, self.y) == (other.x, other.y)
  def __repr__(self):
    return "PTR(%s, %s)" %(self.x, self.y)
print(PTR(1,2) == PTR(1,4))
up = PTR(0, -1)
down = PTR(0, 1)
left = PTR(-1, 0)
right = PTR(1, 0)
directions = [up, down, left, right]

def path(map, M, N):
  def dump():
    for row in map: print(row)
    print("===")
  dump()

  def dfs(pos, cnt=1):
    if pos.x not in range(M) or pos.y not in range(N):
      return
    if map[pos.x][pos.y]: return
    map[pos.x][pos.y] = cnt
    for d in directions:
      dfs(pos+d, cnt+1)

  def bfs(pos=PTR(0,0)):
    queue = [(pos, 1)]
    while queue:
      pos, cnt = queue.pop(0)
      if pos.x not in range(M) or pos.y not in range(N):
        continue
      if map[pos.x][pos.y]:
        continue
      map[pos.x][pos.y] = cnt
      for d in directions:
        queue.append((pos+d, cnt+1))


  #dfs(PTR(0,0))
  bfs()
  dump()

if __name__ == '__main__':
  print(path(labirinth, 4, 5))

