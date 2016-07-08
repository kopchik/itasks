#!/usr/bin/env python3

def isUgly(num):
    dividers = [2,3,5]
    while True:
        for divider in dividers:
            if num % divider == 0:
                num //= divider
                break
        else:
            return num != 1

if __name__ == '__main__':
  print(isUgly(-2147483648))
  
