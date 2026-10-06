# Write a Python program to read and print the contents of the file sample.txt line by
# line.

file = open("sample.txt", "r")

for line in file:
    print(line, end="")

file.close()