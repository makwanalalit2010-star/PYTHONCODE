'''Check if a string starts with "Hello" and ends with "World"

-Remove all non-alphabetic characters from "Data123@Science!"

Reverse the string "Python"'''

text = input("enter a string:")

print("start with 'hello':",text.startswith("hello"))
print("ends with 'world':",text.endswith("world"))

text2 = "Data123@Science!"
result = ""

for ch in text2:
    if ch.isalpha():
        result += ch

print("original string:",text2)
print("after removing non-alphabetic characters:",result)

word = "python"
reverse = word[::-1]

print("reversed string:",reverse)