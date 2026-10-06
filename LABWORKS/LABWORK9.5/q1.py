# Q.1
# Create an abstract class Shape with an abstract method area().
# Inherit two child classes Rectangle and Circle, each implementing the area() method.
# Demonstrate that creating an object of Shape directly raises an error.
# Compute and display area for both Rectangle and Circle.


from abc import ABC, abstractmethod


class shape(ABC):

    @abstractmethod
    def area(self):
        pass

class rectangle(shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

        def area(self):
            return self.length * self.width

class circle(shape):

    def __init__(self, radius):
        self.radius = radius

        def area(self):
            return 3.14 * self.radius * self.radius

try:
    s = shape()
except TypeError as e:
    print("error:", e)

r = rectangle(10, 5)
print("area of rectangle:", r.area()) 

c = circle(7)
print("area of circle:", c.area())