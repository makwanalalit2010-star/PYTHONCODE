# Write a Python program that reads a text file and counts the total number of words,
# characters, and lines in the file.


file = open("notes.txt", "r")

content = file.read()

characters = len(content)

words = len(content.split())

lines = len(content.splitlines())

print("Total Words:", words)
print("Total Characters:", characters)
print("Total Lines:", lines)

file.close()
