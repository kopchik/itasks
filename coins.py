#!/usr/bin/env python3

coins = [
  (50, 10),
  (10, 10),
  (5, 3)
]

def csum(l):
  return sum(coin*num for coin, num in l)


class NoChange(Exception):
  pass


def change(amount, coins=coins):
  print("called with", amount, coins)
  if amount == 0:
    return []
  if not coins:
    raise NoChange
  coin, num = coins[0]
  i = min(amount//coin, num)
  while i >= 0:
      try:
        return [(coin, i)]+change(amount-i*coin, coins=coins[1:])
      except NoChange:
        pass
      i -= 1
  raise NoChange


def bestchange(amount, coins=coins):
  print("called with", amount, coins)
  if not coins:
    return []
  coin, num = coins[0]
  i = min(amount//coin, num)
  answer = []
  while i >= 0:
      new = [(coin, i)]+bestchange(amount-i*coin, coins=coins[1:])
      if csum(new) == amount:
        return new
      if (amount - csum(new)) < (amount - csum(answer)):
        answer = new
      i -= 1
  print("difference is", amount-csum(answer))
  return answer


if __name__ == '__main__':
  #print(change(65))
  print(bestchange(9, coins=[(5,10),(3,2)]))
