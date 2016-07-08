#!/bin/python3

import sys


time = "12:45:54PM"
hours, sep, rest = time.partition(':')
hours = int(hours)
if time.endswith("AM"):
    if hours == 12:
      hours = 0
else:
  if hours < 12:
    hours += 12

print("{:02}".format(hours)+sep+rest[:-2])
