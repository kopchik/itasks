#!/usr/bin/env python3

from PIL import Image
from math import sin, cos

def zipper(a, b):
  for x in a:
    for y in b:
      yield x,y


class Disk:
  def __init__(self, path):
    self.im = Image.open("04.png")
    self.process()


  def read(self, phi):
    r = self.radius
    self.step = 10 # TODO
    x = (r - self.step*phi) * sin(phi)
    y = (r - self.step*phi) * cos(phi)
    return self.im.getpixel((self.center[0]+x,self.center[0]+y))


  def process(self):
    im = self.im.load()
    w, h = self.im.size
    th = 20
    for x,y in zipper(range(w), range(h)):
      if im[x,y] > th:
        x1 = x
        break

    for x,y in zipper(range(w-1, 0, -1), range(h)):
      if im[x,y] > th:
        x2 = x
        break

    for y, x in zipper(range(h), range(w)):
      if im[x,y] > th:
        y1 = y
        break

    for y, x in zipper(range(h-1, 0, -1), range(w)):
      if im[x,y] > th:
        y2 = y
        break

    self.center = (x2-x1)/2, (y2-y1)/2
    self.radius = (x2 - x1)/2



class RecordPlayer:
  def __init__(self, disk):
    self.disk = disk


if __name__ == '__main__':
  disk = Disk("phono.png")
  print(disk.read(1))
  player = RecordPlayer(disk)