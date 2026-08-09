'''Q.3

Create a program that:

Takes a boolean value (True or False) as input.

Converts the boolean to an integer and a string, and prints all three values.'''

bool_value = input("enter true or false:") == "true"

int_value = int(bool_value)
str_value = str(bool_value)

print("boolean value:", bool_value)
print("integer value:", int_value)
print("string value:",str_value)