'''Write a Python program to demonstrate the use of type casting constructors (int().
float(), str(), and bool()):
Take input from the user as a string.
Convert the string into an integer, a float, and a boolean.
Print the converted values along with their types.'''

value = (input("enter a value:"))

int_value = int(value)
float_value = float(value)
str_value = str(value)
bool_value = bool(value)

print("integer value:",int_value)
print("type:",type(int_value))

print("float_value:",float_value)
print("type:",type(float_value))

print("string_value:",str_value)
print("type:",type(str_value))

print("boolean value:",bool_value)
print("type:",type(bool_value))

