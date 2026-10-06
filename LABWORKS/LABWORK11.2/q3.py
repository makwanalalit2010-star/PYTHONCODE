# Write a program to input a filename from the user, read its content, and handle any file-related exceptions.

# Use the else block to print the file content if no exception occurs

filename = input("enter filename: ")

try:
    file = open(filename, 'r')
    content = file.read()
    file.close()

except FileNotFoundError:
    print("error: file not found")
except PermissionError:
    print("error: permission denied")
else:
    print("file content: ")
    print(content)