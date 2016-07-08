#!/usr/bin/env python3

def maxwin(l, w):
  res = []
  ptr = w
  wmax_pos = -1
  wmax = -1
  print(l)
  while ptr <= len(l):
    e = l[ptr-1]
    print("{w} ptr={ptr} e={e}, wmax={wmax}, wmax_pos={wmax_pos}".format(w=l[ptr-w:ptr], ptr=ptr, e=e, wmax=wmax, wmax_pos=wmax_pos))
    if wmax_pos < ptr - w:
        offset = ptr - w + 1
        slice = l[ptr-w:ptr+1]
        print("!", slice, ptr+1, w)
        wmax = max(slice)
        wmax_pos = slice.index(wmax) + offset
    else:
      if e >= wmax:
        wmax = e
        wmax_pos = ptr-1
    res.append(wmax)
    ptr += 1
  return res

if __name__ == '__main__':
  data = [2, 3, 4, 2, 6, 2, 5, 1]
  window = 3
  #window = 2
  #data = [2, 3, 4]
  print(maxwin(data, window))

