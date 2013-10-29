#!/usr/bin/env python3
from __future__ import print_function

def remove_stopwords(query, stopwords):
  query = filter(lambda x: x not in stopwords, query)
  for q in query: print(q)

if __name__ == '__main__':
  remove_stopwords(["the", "new", "store", "in", "SF"], ["the", "in"])
