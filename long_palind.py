#!/usr/bin/env python3
# http://www.talentbuddy.co/challenge/51e486994af0110af3827b17

def is_palind(s):
  for i in range(len(s)//2):
    if s[i] != s[-i-1]: return False
  return True

def palind(s):
  longest = ""
  for i in range(len(s)):
    for j in range(i+1, len(s)+1):
      if is_palind(s[i:j]) and j-i>len(longest):
        longest = s[i:j]
  return(longest)

data = "abcdxyzyx"
print(palind(data))
