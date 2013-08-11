#!/usr/bin/env python3
import math

class Hash:
  def __init__(self, bits=3):
    self.bits = bits
    #if bits:
    #  self.values = [Hash(bits=bits-1) for x in range(2**bits) if bit]
    self.values = [None for x in range(2**bits)]

  def set(self, key, val, h=None):
    if not h:
      h = self.hash(key)
    idx = self.idx(h)
    self.values[idx] = key

  def self.hash(self, key):
    return hash(key)

  def rm(self, key):

    pass

  def idx(self, h):
    mask = (1<<self.bits) - 1
    return h & mask


  def lookup(self, key):
    pass

if __name__ == '__main__':
  h = Hash(2)
  h.set(1,2)
  h.set(2,2)
  h.set(3,2)
  h.set(1024,2)
