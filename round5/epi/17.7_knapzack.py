#!/usr/bin/env python3
#@ weight, price
items = (
(65, 20),
(35, 8),
(245, 60),
(195, 55),
(65, 40),
(150, 70),
(275, 85),
(155, 25),
(120, 30),
(320, 65),
(75, 75),
(40, 10),
(200, 95),
(100, 50),
(220, 40),
(99, 10),
)

from string import ascii_letters

themap = {}
def label(items):
  for label, item in zip(ascii_letters, items):
    themap[label] = item
label(items)
#print(themap)


cnt = 2
def printer(f):
  def wrap(*args, **kwargs):
    global cnt
    print(">"*cnt, *args, **kwargs)
    cnt += 2
    ret = f(*args, **kwargs)
    cnt -= 2
    print("<"*cnt, ret)
    return ret
  return wrap
import copy
#@printer
def calc(capacity, clocks):
    #print("!", capacity, clocks)
    if not clocks:
      return 0, []
    clock = clocks.pop()
    price, weight = themap[clock]
    value1, sack1 = calc(capacity,  copy.copy(clocks))
    value2, sack2 = calc(capacity-weight, copy.copy(clocks))
    #print(value1, sack1, "===", value2+price, sack2+[clock])
    if value1 > value2+price:
      #print("left")
      return value1, sack1
    ret = (value2+price, sack2 + [clock])
    #print("right", ret)
    return ret



if __name__ == '__main__':
  r = calc(10000, set(themap.keys()))
  #r = calc(10000, set(['a', 'b']))
  print(r)
