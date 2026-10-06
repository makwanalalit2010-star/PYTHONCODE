'''Q.3 Write a program to demonstrate a parameterized constructor in the class Rectangle.
Initialize the length and width using the constructor and calculate the area.'''

class rectangle:
    def __init__(self,length, width):
        self.length = length
        self.width = width

    def calculatearea(self):
        area = self.length * self.width
        print(f"area of rectangle: {area}")

rectangle1 = rectangle(11, 10)

rectangle1.calculatearea()