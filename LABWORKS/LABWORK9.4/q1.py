# Q.1 Write a program to demonstrate polymorphism in functions by defining a function add() that can take either two integers or two strings and perform addition or concatenation.

def add(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    elif isinstance(a, str) and isinstance(b, str):
        return a + b
    else:
        return "invalid input"


print("integer addition:", add(10,20))

print("string concatenation:", add("hello ", "python"))

