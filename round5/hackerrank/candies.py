#!/usr/bin/env python3

raw_input = """3
1
2
2""".split()
raw_input = """10
2
4
2
6
1
7
8
9
2
1""".split()
# 33556
raw_input = open('candies_inpt.txt').read().splitlines()[:20]
raw_input[0] = len(raw_input)-1

def input():
  return raw_input.pop(0)


num = int(input())
grades = []
candies = []
for x in range(num):
  grades.append(int(input()))
  candies.append(1)
print(grades)



for i, (grade_prev, grade_next) in enumerate(zip(grades[:-1], grades[1:])):
  candies_prev = candies[i]
  candies_next = candies[i+1]
  if grade_prev > grade_next and candies_prev <= candies_next:
      candies[i] = candies_next + 1
  elif grade_prev < grade_next and candies_prev >= candies_next:
      candies[i+1] = candies_prev+1
  candies_prev = candies[i]
  candies_next = candies[i+1]

"""
for i, (grade_prev, grade_next) in reversed(list(enumerate(zip(grades[:-1], grades[1:])))):
  candies_prev = candies[i]
  candies_next = candies[i+1]
  if grade_prev > grade_next and candies_prev <= candies_next:
      candies[i] = candies_next + 1
  elif grade_prev < grade_next and candies_prev >= candies_next:
      candies[i+1] = candies_prev+1
  candies_prev = candies[i]
  candies_next = candies[i+1]
"""

print("result")
for g,c in zip(grades, candies):
  print("{:<6} {:<6}".format(g,c))
print("grades: ", grades)
print("candies:", candies)
print(sum(candies))
