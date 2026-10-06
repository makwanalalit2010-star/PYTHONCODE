# Question: Create a program to demonstrate Single Inheritance where a class Parent has a method display(), and a child class Child inherits and calls this method.

class parent:
    def display(self):
        print("this is a parent class")

class child(parent):
    pass

obj = child()
obj.display()

