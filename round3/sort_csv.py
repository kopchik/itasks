#!/usr/bin/env python3

data = open("sort_csv.csv", "rt")

def keyfunc(string):
  third_field = string.split()[2]
  return int(third_field)

result = sorted(data, key=keyfunc)
for line in result:
  print(line, end='')


print("=== same but less code ===")
result = sorted(open("sort_csv.csv"),
                key=lambda s: int(s.split()[2]))
[print(line, end='') for line in result]
