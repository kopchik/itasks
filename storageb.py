#!/usr/bin/env python3
from threading import Thread
from os import listdir
from time import time
KiB = 1024
MiB = 1024*KiB
GiB = 1024*MiB
BLKSIZ = 1024*KiB
MINREAD = 1024*KiB
RAM = 4*GiB
NET = 120*MiB  # per second
VRATE = 333*KiB
IOSPEED = 50*MiB
IOSEEK = 0.01

class Worker(Thread):
  def run(self, req):
    t = time()

if __name__ == '__main__':
  MAXCLIENTS = NET/VRATE
  print("network throughtput", MAXCLIENTS)
  print("buffer per client", RAM/MAXCLIENTS)
  if IOSPEED < NET:
    print("**the speed is seriosly limited by HDD")
