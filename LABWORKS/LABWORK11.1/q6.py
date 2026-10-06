# <!-- Write a Python program to open a file in binary mode.
# Q.6
# - Use rb mode to read the content of a text file and display its content in binary format. -->

file = open("notes.txt", "rb")

content = file.read()

print(content)

file.close