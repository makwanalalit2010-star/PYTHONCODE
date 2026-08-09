'''Q.5

Create a program that:

Declares two variables with the same value.

Prints their memory addresses using id() and checks if they are the same.

Modifies one of the variables and checks the memory addresses again.'''

name = "lalit"
name1 = "lalit"

print("id of name:",id(name))
print("id of name1:",id(name1))
print("same memory add:",id(name) == id(name1))

name1 = "rahul"

print("id of name:",id(name))
print("id of name1:",id(name1))
print("same memory address:",id(name) == id(name1))
