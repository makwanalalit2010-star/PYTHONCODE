'''Q.16 Implement a program to create a function that returns a tuple containing the square and cube of a given number.
'''

# def square_and_cube(num):
#     square =num ** 2
#     cube = num ** 3

#     return(square,cube)

# n = int(input("enter a number: "))

# result = square_and_cube(n)

# print("square =", result[0])
# print("cube =", result[1])

def square_cube(num):
    return num**2, num**3

n = int(input("Enter a number: "))

square, cube = square_cube(n)

print("Square =", square)
print("Cube =", cube)