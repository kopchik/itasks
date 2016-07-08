#!/usr/bin/env python3

weights = [2, 2 ,4, 5]
cost    = [3, 7, 2, 9]

def zack(maxweight, pos=0):
  if maxweight == 0 or pos >= len(weights):
    return 0

  cost1 = zack(maxweight, pos+1)
  if weights[pos] > maxweight:
    return cost1
  cost2   = cost[pos] + zack(maxweight-weights[pos], pos+1)
  return max(cost1, cost2)


if __name__ == '__main__':
  print(zack(5))
  
