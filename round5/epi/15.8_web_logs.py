#!/usr/bin/env python3


from collections import defaultdict
db = defaultdict(int)


def add(db, entry):
  db[entry] += 1

def common(db, n):
  return db.items().sort(key = lambda k,v: v)[0:n]

if __name__ == '__main__':
  
  
