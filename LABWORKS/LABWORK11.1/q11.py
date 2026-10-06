# Create a Python program to demonstrate all modes (r, w, a, r+, w+, a+). For each
# mode:

# - Open a file, Write or read content depending on the mode.
# - Close the file properly.

file = open("demo.txt", "w")
file.write("this is wmode.\n")
file.close()

file = open("demo.txt", "r")
print("r mode:")
print(file.read())
file.close()

file = open("demo.txt", "a")
file.write("this is a mode.\n")
file.close()

file = open("demo.txt", "r+")
print("r+ mode:")
print(file.read())
file.write("this is r+ mode.\n")
file.close()

file = open("demo2.txt", "w+")
file.write("this is w+ mode.\n")
file.seek(0)
print(file.read())
file.close()

file = open("demo2.txt", "a+")
file.write("this is a+ mode.\n")
file.seek(0)
print("a+ mode:")
print(file.read())
file.close()