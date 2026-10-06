# Question: Write a program that tries to access an element in a string at a non-existent index. Handle exceptions, and use the else block to print the result if no exception occurs.

text = "hello world"

try:
    index = int(input("enter index:"))
    result = text[index]

except IndexError:
    print("error: index does not exist.")

except ValueError:
    print("error: please enter a valid integer index.")

else:
    print("character:", result)