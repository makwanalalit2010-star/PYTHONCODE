'''Write a recursive function to calculate the factorial of a given number.

Ensure the program handles edge cases (e.g., negative inputs).'''

def factorial(n):

    if n < 0:
        return "factorial does not exist for negative numbers."

    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    

num = int(input("enter a number:"))

print("factorial =",factorial(num))
