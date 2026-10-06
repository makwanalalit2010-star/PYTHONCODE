# Create a Python program that writes multiple lines of text to a file named notes.txt.
# - The content should be:
# Line 1: Python is easy to learn.
# Line 2: It has numerous libraries.
# Line 3: File handling is one of its features.

file = open("notes.txt", "w")

file.write("line1: python is easy to learn.\n")
file.write("line2: it has numerous libraries.\n")
file.write("line3: file handling is one of its features.")

file.close()

print("data written successfully")