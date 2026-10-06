# Write a Python program to append "Line 4: Python supports multiple modes of file

# handling." to the file notes.txt.

file = open("notes.txt", "a")

file.write("\nline 4: python supports multiple modes of file handling.")

file.close()

print("line 4 added successfully")