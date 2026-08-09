'''Implement a program that:

Takes three integers as input.

Uses an if-elif-else' statement to find and print the largest mumber'''

num1 = int(input("enter first num:"))
num2 = int(input("enter second num"))
num3 = int(input("enter third num:"))

if num1 >= num2 and num1 >= num3:
    print("num1 is largest:")
elif num2 >= num1 and num2 >= num3:
    print("num2 is largest")
else:
    print("num3 is largest")