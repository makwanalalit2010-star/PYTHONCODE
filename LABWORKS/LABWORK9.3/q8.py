# Develop a program to check if an object is an instance of a particular class using the isinstance() function.

class student:
    def display(self):
        print("student class")


obj = student()

print(isinstance(obj, student))
print(isinstance(obj, int))