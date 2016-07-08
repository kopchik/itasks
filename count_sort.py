#!/usr/bin/env python3
def key(x):
  return x%3


inpt = [3,4,2,1]
count = [0]*10

for x in inpt:
  count[key(x)] += 1

nc = 0
for i, cnt in enumerate(count):
  count[i] = nc
  nc += cnt

#i = 0
#n = len(inpt)
#while i <= n - 2:
#  x = inpt[i]
#  pos = count[key(x)]
#  temp = inpt[i]
#  inpt[pos] = x
#  x = inpt[i]
#  if i==count[key(x)]:
#    i = i+1

i=0
while i<len(inpt):
  e = inpt[i]
  #if count[key(e)]
  if i==count[key(x)]:
    i = i+1
  tmp = inpt[count[key(e)]]
  count[key(e)] -= 1
  inpt[count[key(e)]] = e
  inpt[i] = tmp

print(inpt)
print(count)
if __name__ == '__main__':
  pass
  
