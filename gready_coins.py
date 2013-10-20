#!/usr/bin/env python3
from copy import copy

def greedy(amount_, coins):
  amount = amount_
  solution = []
  pos = 0
  while l:
    c = coins[pos]
    pos += 1
    while sum(solution) - amount >= c:
      solution += [c]
  print("solution", solution, amount-sum(solution))
  if sum(solution) != amount and len(coins) > 1:
    solution2 = greedy(amount_, l_[1:])
    return solution2, amount2 if solution2 < solution else solution, amount
  return solution, amount

if __name__ == '__main__':
  coins = [100, 50, 20, 10, 5, 2, 1]
  for x in range(1, 101):
    r, rest = greedy(x, coins)
    assert rest == 0
