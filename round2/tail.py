#!/usr/bin/env python3

def readback(f, blksiz):
  # TODO: unaligned IO
  seek = f.seek(0, 2)
  while True:
    prevseek = seek
    seek = max(0, seek - blksiz)
    f.seek(seek)
    yield f.read(prevseek-seek)
    if not seek:
      break


def tail(f, lines=1):
  # assumming file end with new line.
  num_lines = 0
  chunks = []
  it = readback(f, 10)
  for chunk in it:
    chunks.append(chunk)
    num_lines += chunk.count('\n')
    if num_lines > lines:  # strictly > to avoid truncated first line
      break
  buf = "".join(reversed(chunks))
  return buf.splitlines()[-lines:]



if __name__ == '__main__':
  f = open("/etc/resolv.conf", 'rt')
  r = tail(f, 1)
  print(r)
