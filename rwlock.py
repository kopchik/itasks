#!/usr/bin/env python3

from threading import Thread, Lock, BoundedSemaphore, Event
from queue import Queue

from random import randint
import time


class Dummy:
  def __enter__(self, *args, **kwargs):
    pass
  def __exit__(self, *args, **kwargs):
    pass
  def acquire(self):
    pass
  def release(self):
    pass

#########
# Queue #
#########

READ = 1
WRITE = READ + 1
sem = BoundedSemaphore(2)

class CTX:
  def __init__(self):
    self.sem = sem
    self.start = Event()
    self.end = Event()
  def __enter__(self, *args, **kwargs):
    self.start.wait()
    sem.acquire()
  def __exit__(self, *args, **kwargs):
    sem.release()
    self.end.set()

class RWLock(Thread):
  def __init__(self):
    self.queue = Queue()
    super().__init__()

  def read(self):
    ctx = CTX()
    self.queue.put((READ, ctx))
    return ctx

  def write(self):
    ctx = CTX()
    self.queue.put((WRITE, ctx))
    return ctx

  def run(self):
    readers = []  # read events
    mode = READ  # current mode
    while True:
      (req, ctx) = self.queue.get()
      if req == READ:
          ctx.start.set()
          readers += [ctx]
          continue
      elif req == WRITE:
        while readers:
          readers.pop().end.wait()
        ctx.start.set()
        ctx.end.wait()
rwlock = RWLock()
rwlock.start()

class MyThread(Thread):
  def run(self):
    while True:
      if randint(0,1):
        with rwlock.read():
          print("reading start")
          time.sleep(0.1)
          print("reading end")
      else:
        with rwlock.write():
          print("writing")
          time.sleep(0.1)
if __name__ == '__main__':
  for x in range(10):
    t = MyThread()
    t.start()
  t.join()


########
# Lock #
########
readers = 0
wlock = Lock()
#wlock = Dummy()
mlock = Lock()
mlock = Dummy()

class MyThread(Thread):
  def read(self):
    global readers, mlock, wlock
    with mlock:
      if readers == 0:
        wlock.acquire()
      readers += 1

    # actual code
    #assert not wlock.is_set()
    assert readers > 0

    with mlock:
      readers -= 1
      if readers == 0:
        wlock.release()


  def write(self):
    global wlock
    with wlock:
      # actual code
      assert readers == 0

  def run(self):
    while True:
      if randint(0, 1):
        self.read()
      else:
        self.write()


for x in range(10):
  t = MyThread()
  t.start()

t.join()
