'''Implement a program to:

Take a string as input.

Print the string reversed, and also print whether it is a palindrome.'''

text = input("enter a string:")

reverse = text[::-1]

print("reversed string:",reverse)
if reverse == text:
    print("the string is palidrome:")
else:
    print("string is not palidrom")