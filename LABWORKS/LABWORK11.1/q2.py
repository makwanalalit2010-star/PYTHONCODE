# Write a Python program to open an existing file in read mode and display its content.

# - Open the file in write mode, overwrite the content, and write a new sentence
# "Learning file handling in Python is fun!".

file = open("sample.txt", "r")

content = file.read()
print("old content:")
print(content)

file.close()

file = open("sample.txt", "w")

file.write("learning file handling in python is fun!")

file.close()

print("new content written successfully.")