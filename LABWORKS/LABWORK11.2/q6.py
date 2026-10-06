# Question: Create a program that performs division. Handle exceptions for invalid inputs and ensure a final message is displayed using the finally block, regardless of the outcome.


try:
    numerator = float(input("Enter numerator: "))
    denominator = float(input("Enter denominator: "))

    result = numerator / denominator

except ValueError:
    print("error: please enter valid numbers.")

except ZeroDivisionError:
    print("error: division by zero is not allowed.")

else:
    print("return value:", result)

finally:
    print("operation completed.")

