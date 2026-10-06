# Question: Write a program to list all the attributes and methods of a class using the dir() function.


class student:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("student name:", self.name)

obj = student("lalit")
print(dir(obj))