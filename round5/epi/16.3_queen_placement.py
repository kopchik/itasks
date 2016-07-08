#!/usr/bin/env python3

# X Y
def place(n, m, cols=tuple()):
  if m == 0:
    print("result", cols)
    return
  cur_row = len(cols)
  print(cols, cur_row)
  for col in range(n):
    if col in cols:
      continue
    ignore = False
    for row, c in enumerate(cols):
      if c + (cur_row - row) == col:
        ignore = True
        break
      if c - (cur_row -row) == col:
        ignore = True
        break
    if ignore:
      continue
    place(n, m-1, cols=cols+(col,))
  else:
    return


if __name__ == '__main__':
  print(place(4,4))
  
