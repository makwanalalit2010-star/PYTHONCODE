'''Split "apple,banana grapes" into a list

Join the list ["Python", "is", "awesome"] into a sentence using spaces.

Split a multiline string into separate lines and print them one by one.'''

fruits = "apple,banana,grapes"
fruit_list = fruits.split(",")

print("fruit_list:",fruit_list)

word = ["python","is","awesome"]
sentence = " ".join(word)
print("joined sentence:",sentence)

text = """welcome to python learning strings have a nice day"""

lines = text.splitlines()

print("lines:")
for line in lines:
    print(line)