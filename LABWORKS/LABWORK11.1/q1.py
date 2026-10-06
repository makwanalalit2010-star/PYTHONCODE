# Write a Python program to create a text file named sample.txt.

# - Write the sentence "Python is a versatile programming language." into the file.


file = open("sample.text", "w")

file.write("python is a versatile programming language")

file.close()

print("data written successfully")