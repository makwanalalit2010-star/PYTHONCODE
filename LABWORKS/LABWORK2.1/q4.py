'''Write a Python program to:

Take a number as input from the user and check whether it is a neutral number or not using a ladder if statement.'''

num = int(input("enter a number:"))

if num > 0:
    print("the number is positive:")
elif num < 0:
    print("the number is negetive:")
elif num == 0:
    print("the number is neutral:")