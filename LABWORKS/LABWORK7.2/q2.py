'''Q.2 Implement a recursive function to calculate the nth Fibonacci number.'''

def fibonacci(n):

    if n <= 0:
        return "invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
n = int(input("enter the position of the fibonaci number: "))
print("fibonacci number at position",fibonacci(n))