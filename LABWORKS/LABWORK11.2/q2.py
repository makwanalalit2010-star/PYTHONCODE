# # Write a program that tries to access an element in a list at a non-existent index.
# # - Handle the exception using try ... except.

# num = [10,20,30,40,50]

# try:
#     index = int(input("enter index:"))
#     print("element:", num[index])

# except IndexError:
#     print("error: index does not exist in the list.")


num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")