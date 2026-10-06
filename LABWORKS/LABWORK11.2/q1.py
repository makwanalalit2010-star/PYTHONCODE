# Develop a program that divides two numbers provided by the user.
# - Use try ... except to handle division by zero.

try:
    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))

    ans = num1 / num2

    print("ans:", ans)

except ZeroDivisionError:
    print("error: cannot divide by zero")