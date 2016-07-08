#!/usr/bin/env python3

"""
Problem: There are n houses built in a line, each of which contains some value in it. A thief is going to steal the maximal value in these houses, but he cannot steal in two adjacent houses because the owner of a stolen house will tell his two neighbors on the left and right side. What is the maximal stolen value?
"""

def max_stolen_value(houses):
  amount = 0
  for i, house in enumerate(houses):
    




test_data = [6, 1, 2, 7]
print(max_stolen_value(test_data))
