#!/usr/bin/env python3
import re

def strip(s):
  #return re.sub(r"\/\*.*\*\/", '', s)
  return re.sub(r"/\/*(.|\n)*\*\/", '', s, flags=re.M)

if __name__ == '__main__':
  data = "hello /* this is a\nmulti line comment */ all"
  print(strip(data))
