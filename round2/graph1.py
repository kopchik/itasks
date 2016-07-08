#!/usr/bin/env python3

graph = {
  'a': ['b', 'c'],
  'b': ['d', 'e'],
  'c': ['f', 'g']
}
print(graph)


def traverse(queue):
  newqueue = []
  for i in range(len(queue)):
    node = queue.pop(0)
    print(node)
    if node in graph:
      queue.extend(graph[node])
  if queue:
    traverse(queue)

traverse(['a'])
