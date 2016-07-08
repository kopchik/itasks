#!/usr/bin/env python3


def get_max_profit(data):
  min_buy_prices = [data[0]]
  max_sell_prices = [data[-1]]
  for e in data[1:]:
    if e < min_buy_prices[-1]:
      min_buy_prices.append(e)
    else:
      min_buy_prices.append(min_buy_prices[-1])

  for e in reversed(data[:-1]):
    print(e)
    if e > data[0]:
      max_sell_prices.insert(0, e)
    else:
      max_sell_prices.insert(0, max_sell_prices[0])

  print(min_buy_prices)
  print(max_sell_prices)
  max_profit = 0
  for buy, sell in zip(min_buy_prices[:-1], max_sell_prices[1:]):
    profit = sell - buy
    if profit > max_profit:
      print("!", sell, buy)
      max_profit = profit
  print(max_profit)
  return max_profit


def get_max_profit_smart(data):
  max_price, max_price_pos = data[1], 1
  min_price, min_price_pos = data[0], 0
  max_profit  = max_price - min_price
  for i in range(2, len(data)):
    e = data[i]
    if e > max_price:
      max_price = e
      max_price_pos = i
      max_profit_new = max_price - min_price
      if max_profit_new > max_profit:
        max_profit = max_profit_new
    elif e < min_price:
      min_price, min_price_pos = e, i
      max_price, max_price_pos = 0, 1

    if max_price_pos > min_price_pos:
      new_profit = max_price - min_price
      if new_profit > max_profit:
        max_profit = profit
  print(max_profit)



if __name__ == '__main__':
  stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
  get_max_profit_smart(stock_prices_yesterday)


