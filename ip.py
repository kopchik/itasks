def valid(args):
  return all(o in range(0,256) for o in args) and len(args) == 4

def merge(nums):
  return sum(n*(10**i) for i,n in (enumerate(reversed(nums))))

def try1(a):
  if not a: yield []
  for i,_ in enumerate(a,1):
    for p in try1(a[i:]):
      yield [merge(a[:i])] + p


data=[2,5,5,2,5,5,2,5,5,2,5,5]
for ip in try1(data):
  if valid(ip):
    print(ip)
