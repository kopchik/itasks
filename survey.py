#!/usr/bin/env python3

from random import SystemRandom
from collections import Counter
from statistics import median

r = SystemRandom()
random = r.random

def experiment():
  surveys = []
  i = 0
  while len(surveys) < 200:
    i += 1
    #if random() < 0.1:
    #  i += 1
    #elif random() < 0.2:
    #  i += 2
    if random() <0.3:
      continue
    survey = i % 3
    surveys.append(survey)
  #surveys = [survey for survey in surveys if random() <0.7]
  cnt = Counter(surveys)
  return cnt[0], cnt[1], cnt[2]


if __name__ == '__main__':
  data = [experiment() for i in range(1000)]
  for i in range(3):
    dset = [d[i] for d in data]
    print("median: {median}, max: {max}, min: {min}".format(median=median(dset), min=min(dset), max=max(dset)))
