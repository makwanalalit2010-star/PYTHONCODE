# Q.4 Write a program using try-except-else-finally that divides two numbers entered by the user.

try:
    a = float(input("enter first number:"))
    b = float(input("enter second number:"))

    result = a / b

except ValueError:
    print("error: please enter valid numbers")

except ZeroDivisionError:
    print("error: cannot divide by zero")

else:
    print("division result:", result)

finally:
    print("program completed")

    