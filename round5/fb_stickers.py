#!/usr/bin/env python3

"""
Facebook logo stickers cost $2 each from the company store. I have an idea. I want to cut up the stickers, and use the letters to make other words/phrases. A Facebook logo sticker contains only the word 'facebook', in all lower-case letters.

Write a function that, given a string consisting of a word or words made up of letters from the word 'facebook', outputs an integer with the number of stickers I will need to buy. foo('coffee kebab') -> 3 foo('book') -> 1 foo('ffacebook') -> 2

You can assume the input you are passed is valid, that is, does not contain any non-'facebook' letters, and the only potential non-letter characters in the string are spaces.
"""


from collections import defaultdict, Counter
from math import ceil
bucket = Counter('facebook')
def cost(s):
  s = s.replace(' ','')
  return ceil(max(cnt/bucket[c] for c, cnt in Counter(s).items()))

if __name__ == '__main__':
  print(cost('coffee kebab'))
  
