# Create a program using polymorphism where an interface Transport has a method travel().
# - Implement it differently in classes Train and Plane.

from abc import ABC, abstractmethod

class transport(ABC):
    @abstractmethod
    def travel(self):
      pass

class train(transport):
  def travel(self):
    print("traveling by train")

class plane(transport):
  def travel(self):
    print("traveling by plane")

t1 = train()
t2 = plane()


t1.travel()
t2.travel()