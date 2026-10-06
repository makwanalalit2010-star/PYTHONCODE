# Write a Python program to read content from an existing file source.txt and copy it to a new file backup.txt

source = open("source.txt", "r")

content = source.read()

source.close()

backup = open("backup.txt", "w")

backup.write(content)

backup.close()

print("content copied successfully.")