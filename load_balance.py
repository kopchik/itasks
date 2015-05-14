#!/usr/bin/env python3

from threading import Thread
from queue import Queue
from time import sleep, time
from collections import defaultdict, deque
from statistics import mean


class Worker(Thread):
  def __init__(self, replies, latency):
    super().__init__()
    self.replies = replies
    self.latency = latency
    self.queue = Queue()
    self.daemon = True

  def run(self):
    while True:
      r = self.queue.get()
      sleep(self.latency)
      self.replies.put((self, r))

  def __repr__(self):
    return "W:%s" % self.latency


class Load(Thread):
  def __init__(self, workers, latencies):
    super().__init__()
    self.workers = workers
    self.latencies = latencies
    self.queue = Queue()

  def run(self):
    latencies = self.latencies
    while True:
      #key = lambda w: latencies[w]
      key = lambda w: (w.queue.qsize() / w.latency)
      backend = min(self.workers, key=key)
      now = time()
      backend.queue.put(now)
      sleep(0.00035)


class Sink(Thread):
  def __init__(self, queue, latencies, workers):
    super().__init__()
    self.queue = queue
    self.latencies = latencies
    self.workers = workers

  def run(self):
    stat = deque(maxlen=10)
    lstat = []
    lstat_ts = time()
    while True:
      w, r = self.queue.get()
      now = time()
      latency = now - r
      self.latencies[w] = latency
      stat.append(latency)
      lstat.append(latency)
      #print("latency: {:.2f} from {}".format(latency, w))
      #print("mean:", mean(stat))
      if len(lstat) > 1000:
        print("avg qlen:", mean(w.queue.qsize() for w in self.workers))
        print("qps:", len(lstat) / (now - lstat_ts))
        lstat = []
        lstat_ts = now
      #print(self.latencies)


if __name__ == '__main__':
  workers = []
  replies = Queue()
  latencies = defaultdict(lambda: 0)
  for _ in range(100):
    for x in range(1,10):
      w = Worker(replies=replies, latency=x/1000)
      w.start()
      workers.append(w)
  load = Load(workers=workers,latencies=latencies)
  load.start()
  sink = Sink(queue=replies, latencies=latencies, workers=workers)
  sink.start()
  sink.join()
