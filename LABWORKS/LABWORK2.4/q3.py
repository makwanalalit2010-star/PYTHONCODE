'''create a program that:
iterates over a string(e.g,"python")
uses a continue statment to skip vowels and print only constants'''

a="PYTHON"
for i in a:
    if i in "aeiouAEIOU":
        continue
    print(i)