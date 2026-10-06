# <!-- Q.5: Write a program to demonstrate method overloading by creating a class Calculator with a method multiply() that works for two or three arguments.
# - Use default arguments or variable-length arguments. -->

class calculator:
    def multiply(self, a, b, c=1):
        return a * b * c

cal = calculator()


print("multilpication of 2 numbers:", cal.multiply(5, 4))

print("multiplication of 3 numbers:", cal.multiply(5, 4, 2))
    