#!/usr/bin/env python3
from __future__ import print_function
def tokenize_query(query, punctuation):
  t = str.maketrans(punctuation, " "*len(punctuation))
  [print(chunk) for chunk in query.translate(t).split()]
if __name__ == '__main__':
  query = "car? dealers! bmw, audi"
  punctuation = "?!"
  tokenize_query(query, punctuation)
