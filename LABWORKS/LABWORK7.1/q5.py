'''Create a program that takes a user-defined function as an argument to calculate the cube of a list of numbers.'''

def cube(x):
    return x ** 3

def calculate(func, numbers):
    result = []

    for i in numbers:
        result.append(func(i))

    return result

lst = [2, 3, 4, 5]

print(calculate(cube, lst))