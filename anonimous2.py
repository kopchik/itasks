#!/usr/bin/env python3

class Parent:
  def say_b(self):
    print(self.b)

class Child(Parent):
  pass

obj = Child()
obj.b = "surprise"

Parent.say_b = lambda self: print(self.b+"foo")

obj.say_b()
