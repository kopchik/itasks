#!/usr/bin/env python3


def remove_substring(s, p, n):
    def cut(s,p,n,c):
        if len(s) == 1:
            return ""
        if c>=p-1 and c<p+n-1:
          print("!", s[0])
          return cut(s[1:],p,n,c+1)
        else:
          print(s[0])
          return s[0]+cut(s[1:],p,n,c+1)
    print(cut(s,p,n,0))


remove_substring("abcdefghi ", 4,3)
