#!/usr/bin/env python3
from collections import defaultdict

def find_closest_car(city_map, cars, customer):
  carset = set(cars)
  graph = {}
  adjmap = defaultdict(list)
  costmap = {}
  for raw in city_map:
    node1, node2, lenght = [int(i) for i in raw.split(',')]
    graph[node1, node2] = graph[node2, node1] = lenght
    adjmap[node1].append(node2)
    adjmap[node2].append(node1)
  def dijkstra(src, dst, cost):
    if dst not in costmap:
      costmap[dst] = cost
    elif costmap[dst] < cost:
      return
    costmap[dst] = cost
    src = dst
    for dst in adjmap[dst]:
      if dst == src:
        continue
      nextcost = cost + graph[src, dst]
      dijkstra(src, dst, nextcost)
  dijkstra(customer, customer, 0)
  
  for candidate in sorted(costmap):
    if candidate in carset:
      print(cars.index(candidate))
      break

  

if __name__ == '__main__':
  city_map = ["1,2,2", "6,2,2", "6,4,1", "5,4,1", "2,5,1", "5,3,1", "2,3,2"]
  cars = [1, 6]
  customer = 3
  #find_closest_car( ["1,2,1", "2,3,2", "1,3,1", "3,4,1"], [2,1], 4)
  find_closest_car(city_map, cars, customer)
