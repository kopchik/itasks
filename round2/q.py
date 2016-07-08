class FullError(Exception):
  """ When queue is full. """


class EmptyError(Exception):
  """ When queue is empty. """


class Q:
  def __init__(self, maxsize):
    self.array = [None for _ in range(maxsize)]
    self.head = 0
    self.tail = 0
    self.maxsize = maxsize
    self.size = 0

  def push(self, value, displace=False):
    if self.size == self.maxsize:
      if displace:
        self.pop()
      else:
        raise FullError("queue full")
    self.array[self.head] = value
    self.size += 1
    self.head = (self.head + 1) % self.maxsize

  def pop(self):
    if not self.size:
      raise EmptyError("queue empty")
    value = self.array[self.tail]
    self.array[self.tail] = None
    self.size -= 1
    self.tail = (self.tail + 1) % self.maxsize
    return value

  def as_array(self):
    result = []
    while self.size:
      result.append(self.pop())
    return result

def expect(exc, f, *args):
  try:
    f(*args)
    raise Exception("expected %s, got nothing" % exc)
  except exc:
    return
  except Exception as err:
    raise Exception("expected %s, got %s" % (exc, err))

size = 3
q = Q(size)

for i in range(size):
  q.push(i)
assert q.size == size
assert q.array == [0,1,2]

expect(FullError, q.push, 4)

assert [q.pop() for _ in range(size)] == [0,1,2]

q.push(0)
q.push(1)
assert q.as_array() == [0,1]

q.push(0)
q.push(1)
q.push(2)
q.push(3, displace=True)
assert q.as_array() == [1,2,3]

