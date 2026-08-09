'''Take a number as input from the user.

Use an 'if-else' statement to check if the number is even or odd and print the result.'''

num = int(input("enter number:"))

if num % 2 == 0:
    print(num,"even")
else:
    print(num,"odd")