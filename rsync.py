#!/usr/bin/env python3
from sys import argv, stderr
from zlib import adler32
from hashlib import md5

def strong(data):
  m = md5()
  m.update(data)
  return m.hexdigest()

def weak(data):
  return adler32(data)

def weak(data):
  return sum(data)%2

def roll(a, value, b):
  return (value - a + b) % 2



def dbg(*args, **kwargs):
  if __debug__:
    print(*args, file=stderr, **kwargs)


def diff(src, dst, size=1024):
  blkref = {}
  weaks = set()

  # calculate blocks and maps
  for start in range(0, len(src), size):
    chunk = src[start:start+size]
    stronghash = strong(chunk)
    weakhash = weak(chunk)
    weaks.add(weakhash)
    blkref[weakhash,stronghash] = chunk
  print("done processing src file")
  dbg("weak hashes:", weaks)
  dbg("block references", blkref)
  dbg()

  ptr = 0
  weakhash = stronghash = None
  diffbytes = []
  diffstart = diffend = None
  dstlen = len(dst)
  collisions = 0
  while ptr < dstlen:
    chunk = dst[ptr:ptr+size]
    dbg("chunk:", chunk)
    #if not weakhash or ptr+size > dstlen:
    if True:
      weakhash = weak(chunk)
      dbg("weakhash={weakhash}".format(**locals()))
    else:
      dbg("prev:", dst[ptr-1], "last:", dst[ptr+size-1])
      weakhash = roll(dst[ptr-1], weakhash, dst[ptr+size-1])
      dbg("weakhash={weakhash} (rolling)".format(**locals()))
      #assert weakhash == weak(chunk)
    if weakhash in weaks:
      stronghash = strong(chunk)
      if (weakhash,stronghash) in blkref:
        dbg("block found!")
        ptr += size
        weakhash = None  # because we jumped for `size' bytes and rolling csum won't work
        if diffstart is not None:
          diff = dst[diffstart:diffend+1]
          diffbytes.append( (diffstart, diffend, diff) )
          diffstart = diffend = None
        continue
      else:
        dbg("!! false weakhash hit")
        collisions += 1
    # block differs
    print("detected difference in pos", ptr, "({%s})"%chr(dst[ptr]))
    if diffstart is None:
      diffstart = diffend = ptr
    else:
      diffend += 1
    ptr += 1

  if diffstart is not None:
    diffbytes.append( (diffstart, diffend, diff) )
  print("Number of collisions:", collisions)
  print("Number of weak checksums:", len(weaks))
  print("blocks not present in src:", diffbytes)


if __name__ == '__main__':
  #src = open(argv[1], "rb").read()
  #dst = open(argv[2], "rb").read()
  #src = memoryview(src)
  #for ptr in range(0, 12*1024*1024):
  #  weak(src[ptr:ptr+1024])
  #dst = memoryview(dst)
  #diff(src, dst, size=128)

#TODO: dst does not use all blocks
#TODO:
  diff(b"123", b"1239123abcdbrwrfdadaedfwfrg", size=1)
