#!/usr/bin/env python3
from sys import argv, stderr
from zlib import adler32
from hashlib import md5

MOD_ADLER = 65521

def strong(data):
  """ calculate strong csum """
  m = md5()
  m.update(data)
  #return m.hexdigest()
  return m.digest()


def my_slow_adler32(data):
  s1 = 1
  s2 = 0
  for c in data:
    s1 += c
    s2 += s1
  s1 %= MOD_ADLER
  s2 %= MOD_ADLER
  return s2<<16 | s1
weak = adler32


def roll(oldchar, csum, newchar, blksize):
    s1 = csum & 0xffff
    s2 = (csum >> 16) & 0xffff
    s1 = (s1 - oldchar + newchar) % MOD_ADLER
    s2 = (s2 - ((blksize) * oldchar) + s1 - 1) % MOD_ADLER  # -1 is initial value of s1
    return (s2 << 16) | s1


def dbg(*args, **kwargs):
  if __debug__:
    print(*args, file=stderr, **kwargs)


def diff(src, dst, size=1024):
  blkmap = {}
  weaks = set()  # weak checksums

  # build csum=>block mapping
  for start in range(0, len(src), size):
    chunk = src[start:start+size]
    stronghash = strong(chunk)
    weakhash = weak(chunk)
    weaks.add(weakhash)
    blkmap[weakhash,stronghash] = chunk
  print("done processing src file")
  dbg("weak hashes:", weaks)
  dbg("block references", blkmap)
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
    if not weakhash or ptr+size > dstlen:
    #if True:
      # calculate weak hash from scratch
      weakhash = weak(chunk)
      dbg("weakhash={weakhash}".format(**locals()))
    else:
      # reuse old value to calculate a new one (rolling checksum)
      dbg("prev:", dst[ptr-1], "last:", dst[ptr+size-1])
      weakhash = roll(dst[ptr-1], weakhash, dst[ptr+size-1], size)
      dbg("weakhash={weakhash} (rolling)".format(**locals()))
      assert weakhash == weak(chunk)
    if weakhash in weaks:
      stronghash = strong(chunk)
      if (weakhash,stronghash) in blkmap:
        dbg("found block", (weakhash,stronghash))
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
    #print("detected difference in pos", ptr, "({%s})"%chr(dst[ptr]))
    if diffstart is None:
      diffstart = diffend = ptr
    else:
      diffend += 1
    ptr += 1

  if diffstart is not None:
    diff = dst[diffstart:diffend+1]
    diffbytes.append( (diffstart, diffend, diff) )
  print("Number of collisions:", collisions)
  print("Number of weak checksums:", len(weaks))
  print("Number of strong checksums:", len(blkmap))
  print("weak/strong ratio: {:.2f} (bigger is better)".format(len(weaks)/len(blkmap)))
  #print("blocks not present in src:", diffbytes)


if __name__ == '__main__':
  src = open(argv[1], "rb").read()
  dst = open(argv[2], "rb").read()
  src = memoryview(src)
  #for ptr in range(0, 12*1024*1024):
  #  weak(src[ptr:ptr+1024])
  #dst = memoryview(dst)
  diff(src, dst, size=4096)

#TODO: dst does not use all blocks
#TODO:
  #diff(b"123", b"1239123abcdbrwrfdadaedfwfrg", size=1)
