#!/usr/bin/env python3
def debug(*args, **kwargs):
  print("   "*(len(getstack())-2), *args, **kwargs)

def minimum_coins(coins, amount):
  print( min_coins(coins, amount) )

def min_coins(coins, amount):
    best = 99999  # magic value indicating there is no change :)
    if amount == 0: return 0
    if not coins: return best
    for j,c in enumerate(coins, 1):
        i = 0
        while c*i <= amount:
          best = min(best, min_coins(coins[j:], amount-c*i)+i)
          i += 1
    return best

if __name__ == '__main__':
  coins, amount = [10,5,1], 28
  minimum_coins(coins, amount)
