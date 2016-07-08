#!/usr/bin/env python3
import asyncio

@asyncio.coroutine
def worker():
  print("!!!!!!!")
  yield from asyncio.sleep(2)
  print("END1")
  yield from asyncio.sleep(2)
  print("END2")



def myloop(loop, w):
  print("spawned")
  yield from asyncio.sleep(1)
  print("time to die")
  #t.cancel()
  #for f in asyncio.as_completed([w]):
  done, pending = yield from asyncio.wait([t])
  print("waiting done for", done, pending)
  

loop = asyncio.get_event_loop()
w = worker()
t = loop.create_task(w)
loop.create_task(myloop(loop,t))
loop.run_forever()
if __name__ == '__main__':
  pass
  
