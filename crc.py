#!/usr/bin/env python3
from binascii import crc32
from string import printable as charset
#from string import ascii_letters as charset


def gen_salt(deph=2):
  if deph == 0: return ""
  for x in charset:
    print(x+gen_salt(deph-1), end=" ")


charset = [bytes(c, 'ascii') for c in charset]
class Char:
  def __init__(self, num=3):
    self.pos = 0
    self.prefix = b""
    if num: self.child = iter(Char(num-1))
    else:   self.child = None

  def __iter__(self):
    return self

  def __next__(self):
    self.pos += 1
    if self.pos >= len(charset):
      if not self.child:
        raise StopIteration
      self.prefix = next(self.child)
      self.pos = 0
    return self.prefix+charset[self.pos]

c = Char(10)
#while True:
#  print(c.next(), end="|")

def raw2str(v):
  r = []
  while v:
    r += [bytes(v%255)]
    v = v >> 8
  return b"".join(r)

def guess(payload, csum):
  #for rawsalt in range(2**32):
  #  salt = raw2str(rawsalt)
  for i, salt in enumerate(c):
    if not i%1000000: print(salt, end=' ',flush=True)
    if crc32(salt+payload) == csum:
      print("!", salt)


if __name__ == '__main__':
  guess(b'away',0xCB2A3B76)
  guess(b'molt',0x58D674F6)
  guess(b'coat',0x0DA77D88)
  #guess('away',0xCB2A3B76)
