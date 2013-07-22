#!/usr/bin/env python3
from sys import stdin
import sys
import os


def smart_tail(path, lines=10, chunk_size=1024):
  with open(path, "rb") as fd:
    size = os.fstat(fd.fileno()).st_size
    pos = size - chunk_size
    data = b""
    while True:
      if pos > 0: fd.seek(pos)
      else:       fd.seek(0)
      chunk = fd.read(chunk_size)
      data = chunk + data
      line_num = len(data.split(b"\n"))
      if line_num > lines+2 or pos <= 0:
        break
      pos -= chunk_size

  for line in data.split(b"\n")[-(lines+1):-1]:
    print(line.decode())


if __name__ == '__main__':
  if len(sys.argv) != 3:
    sys.exit("please specify file name and chunk size")
  fname = sys.argv[1]
  chunk_size = int(sys.argv[2])
  smart_tail(fname, lines=3, chunk_size=chunk_size)