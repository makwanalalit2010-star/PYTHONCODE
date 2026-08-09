'''Write a Program in Python to find the minimum number from the given three numbers using a nested if statement.
'''
a = 16
b = 23
c = 30

if a < b:
    if a < c:
        print("a is maximum number:")
    else:
        print("c is maximum number:")
else:
    if b < c:
        print("b is maximum number:")
    else:
        print("c is maximum number:")