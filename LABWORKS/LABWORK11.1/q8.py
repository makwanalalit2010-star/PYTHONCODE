# Write a Python program to open a text file in read-write mode.
# - Read the existing content.
# - Append the line "This file was last modified by adding this sentence." to the file.

file = open("notes.txt", "r+")

content = file.read()

print("existing content:")
print(content)

file.seek(0, 2)

file.write("\n this file was last modified by adding this sentence.")

file.close()

print("new sentence added successfully")