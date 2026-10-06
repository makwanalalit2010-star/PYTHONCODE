# Write a program that prompts the user to enter a number and attempts to find its square root. Use try to handle invalid input (e.g., negative numbers), else to print the square root if successful, and finally to display a message like "Execution complete."



try:
    number = float(input("Enter a number: "))
    if number < 0:
        raise ValueError("Invalid input: please enter a non-negative number.")
    square_root = math.hypot(number, 0)  # Using math.hypot for square root
except ValueError as e:
    print("Error:", e)
else:
    print("Square root:", square_root)
finally:
    print("Execution complete.")