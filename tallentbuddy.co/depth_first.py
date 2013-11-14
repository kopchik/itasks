#!/usr/bin/env python3

tree = "puvetnarynapl ieu issklnl a eetNv,nra rmtc,ae eigi daateot m g.***e* *d***n*c*c***a*e* *** *s*e*** *l*a*** *x*i***n*h*s***n*h**"
tree = "w   snulnmrmunandsi oatsitit tdKoegi onata   u;id so tni  fi l.***w***e***k*w*g***o*t*i***f*i* ***o*** ***p*t*g***i*a*r***s*a**"

def visit(tree, n=1):
  if n >= len(tree) or tree[n-1] == '*':
    return []
  return \
  visit(tree, n*2) + [tree[n-1]] + visit(tree,n*2+1)

if __name__ == '__main__':
  print("".join(visit(tree)))
