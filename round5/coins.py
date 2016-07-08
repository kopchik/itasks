#!/usr/bin/env python3


def change1(amount, coins):
  print(amount, coins)
  for coin in coins:
    if coin == amount:
      return [coin]
    if coin > amount:
      continue
    newchange = change(amount-coin, coins)
    if newchange is None:
      continue
    return [coin] + newchange
  return None

cache = {}
def change(amount, coins):
  if amount == 0:
    return []
  coin = max(c for c in sorted(coins) if c<= amount)
  num = amount // coin
  if num*coin == amount:
    return [coin]*num
  for n in range(num, 0, -1):
    try:
      r = change(amount - n*coin, coins-set([coin]))
      return  [coin]*num + r
    except Exception:
      continue
  raise Exception("no change")


if __name__ == '__main__':
  #change(10000, set([3,2,2]))
  print(change(100000, set([3,2])))
  
