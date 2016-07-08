#!/usr/bin/env python3

a = [1,2,3,5]

for i,j in zip(a, range(a[0], a[-1])):
  if j != i:
    print(j)
    break

#if len(a) % 2:
#  a.append(a[-1] + 1)

actual = sum(a)
pair = a[0] + a[-1]
expected = pair * (len(a) // 2)
if len(a) % 2 == 0:
  expected += pair//2
print(expected-actual)

if __name__ == '__main__':
  pass

