def perm(a):
  if not a: yield []
  for i,c in enumerate(a):
    for p in perm(a[:i] + a[(i + 1):]):
                  yield [c]+p


print(list(perm([1,2,3])))
