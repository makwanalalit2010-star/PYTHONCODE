# Functional Treat
# Python - Data Science
# Data Analyzer and Transformer Program

# Global variables
data = []
dataset_summary = {}


# ---------------------------------------------------------
# A. BUILT-IN FUNCTIONS
# ---------------------------------------------------------

def display_summary():
    """Display basic dataset information using built-in functions."""
    
    if not data:
        print("\nNo data available. Please enter data first.")
        return

    print("\n----- Data Summary -----")
    print("Total elements:", len(data))
    print("Minimum value:", min(data))
    print("Maximum value:", max(data))
    print("Sum of all values:", sum(data))
    print("Average value:", sum(data) / len(data))


# ---------------------------------------------------------
# B. USER-DEFINED FUNCTIONS
# ---------------------------------------------------------

def calculate_average(numbers):
    """Calculate and return the average of a list of numbers."""
    
    if len(numbers) == 0:
        return 0
    
    return sum(numbers) / len(numbers)


def find_duplicates(numbers):
    """Find and return duplicate values from a list."""
    
    duplicates = []
    
    for i in numbers:
        if numbers.count(i) > 1 and i not in duplicates:
            duplicates.append(i)
    
    return duplicates


# ---------------------------------------------------------
# C. *args, **kwargs and __doc__
# ---------------------------------------------------------

def show_args(*args):
    """Accept multiple values using *args and display them."""
    
    print("\nValues received using *args:")
    
    for value in args:
        print(value)


def show_dataset_info(**kwargs):
    """Display dataset information using **kwargs."""
    
    print("\n----- Dataset Characteristics -----")
    
    for key, value in kwargs.items():
        print(key, ":", value)


# ---------------------------------------------------------
# D. RECURSION
# ---------------------------------------------------------

def factorial(n):
    """Calculate factorial of a number using recursion."""
    
    if n == 0 or n == 1:
        return 1
    
    return n * factorial(n - 1)


def fibonacci(n):
    """Calculate Fibonacci number using recursion."""
    
    if n <= 1:
        return n
    
    return fibonacci(n - 1) + fibonacci(n - 2)


# ---------------------------------------------------------
# E. LAMBDA FUNCTION
# ---------------------------------------------------------

def filter_by_threshold(numbers, threshold):
    """Filter values greater than or equal to the threshold."""
    
    result = list(filter(lambda x: x >= threshold, numbers))
    
    return result


def double_values(numbers):
    """Double all values using lambda and map."""
    
    result = list(map(lambda x: x * 2, numbers))
    
    return result


# ---------------------------------------------------------
# F. GLOBAL KEYWORD
# ---------------------------------------------------------

def update_global_summary(numbers):
    """Update the global dataset summary."""
    
    global dataset_summary
    
    dataset_summary = {
        "Total Values": len(numbers),
        "Sum": sum(numbers),
        "Average": calculate_average(numbers),
        "Minimum": min(numbers),
        "Maximum": max(numbers)
    }


def display_global_summary():
    """Display the summary stored in the global variable."""
    
    print("\n----- Global Dataset Summary -----")
    
    for key, value in dataset_summary.items():
        print(key, ":", value)


# ---------------------------------------------------------
# G. RETURN MULTIPLE VALUES
# ---------------------------------------------------------

def dataset_statistics(numbers):
    """Return minimum, maximum, sum and average values."""
    
    minimum = min(numbers)
    maximum = max(numbers)
    total = sum(numbers)
    average = calculate_average(numbers)
    
    return minimum, maximum, total, average


# ---------------------------------------------------------
# H. 1D AND 2D ARRAY / LIST
# ---------------------------------------------------------

def input_1d_data():
    """Take 1D list data from the user."""
    
    global data
    
    values = input("\nEnter 1D array values separated by spaces: ")
    
    data = list(map(int, values.split()))
    
    print("\n1D Data stored successfully!")
    print("Data:", data)
    
    update_global_summary(data)


def input_2d_data():
    """Take 2D nested list data from the user."""
    
    global data
    
    rows = int(input("\nEnter number of rows: "))
    cols = int(input("Enter number of columns: "))
    
    data = []
    
    for i in range(rows):
        row = list(map(int, input(
            f"Enter {cols} values for row {i + 1}: "
        ).split()))
        
        data.append(row)
    
    print("\n2D Data stored successfully!")
    
    display_2d_data()


def display_2d_data():
    """Display a 2D list in grid format."""
    
    if not data:
        print("\nNo data available.")
        return
    
    print("\n----- 2D Data -----")
    
    for row in data:
        for value in row:
            print(value, end="\t")
        print()


# ---------------------------------------------------------
# I. SORTING COLLECTION DATA TYPES
# ---------------------------------------------------------

def sort_1d_data():
    """Sort 1D data in ascending or descending order."""
    
    if not data:
        print("\nNo data available.")
        return
    
    print("\nChoose sorting option:")
    print("1. Ascending")
    print("2. Descending")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        sorted_data = sorted(data)
        print("\nSorted Data in Ascending Order:")
        print(sorted_data)
        
    elif choice == 2:
        sorted_data = sorted(data, reverse=True)
        print("\nSorted Data in Descending Order:")
        print(sorted_data)
        
    else:
        print("\nInvalid choice!")


def sort_2d_data():
    """Sort rows of a 2D list using sorted()."""
    
    if not data:
        print("\nNo data available.")
        return
    
    print("\nOriginal 2D Data:")
    display_2d_data()
    
    sorted_data = sorted(data)
    
    print("\nSorted 2D Data:")
    
    for row in sorted_data:
        print(row)


# ---------------------------------------------------------
# EXTRA FUNCTIONS
# ---------------------------------------------------------

def find_duplicates_menu():
    """Display duplicate values from the dataset."""
    
    if not data:
        print("\nNo data available.")
        return
    
    duplicates = find_duplicates(data)
    
    if duplicates:
        print("\nDuplicate values:", duplicates)
    else:
        print("\nNo duplicate values found.")


def lambda_menu():
    """Perform lambda operations on the dataset."""
    
    if not data:
        print("\nNo data available.")
        return
    
    print("\n----- Lambda Operations -----")
    print("1. Filter values by threshold")
    print("2. Double all values using map()")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        threshold = int(input("Enter threshold value: "))
        
        result = filter_by_threshold(data, threshold)
        
        print("\nValues greater than or equal to", threshold, ":")
        print(result)
        
    elif choice == 2:
        result = double_values(data)
        
        print("\nDoubled values:")
        print(result)
        
    else:
        print("\nInvalid choice!")


def recursion_menu():
    """Perform factorial or Fibonacci operation using recursion."""
    
    print("\n----- Recursion -----")
    print("1. Factorial")
    print("2. Fibonacci")
    
    choice = int(input("Enter your choice: "))
    n = int(input("Enter a number: "))
    
    if choice == 1:
        result = factorial(n)
        print("\nFactorial of", n, "is:", result)
        
    elif choice == 2:
        result = fibonacci(n)
        print("\nFibonacci value at position", n, "is:", result)
        
    else:
        print("\nInvalid choice!")


# ---------------------------------------------------------
# MAIN MENU
# ---------------------------------------------------------

while True:

    print("\n==============================================")
    print(" Welcome to the Data Analyzer and Transformer")
    print("==============================================")

    print("\nMain Menu")
    print("1. Input 1D Data")
    print("2. Input 2D Data")
    print("3. Display Data Summary (Built-in Functions)")
    print("4. Calculate Average")
    print("5. Find Duplicate Values")
    print("6. Recursion (Factorial / Fibonacci)")
    print("7. Filter Data by Threshold (Lambda)")
    print("8. Map Data using Lambda")
    print("9. Sort 1D Data")
    print("10. Sort 2D Data")
    print("11. Display Dataset Statistics (Multiple Return Values)")
    print("12. Display Dataset using *args")
    print("13. Display Dataset Characteristics using **kwargs")
    print("14. Display Function __doc__")
    print("15. Display Global Dataset Summary")
    print("16. Exit Program")

    choice = int(input("\nPlease enter your choice: "))


    # 1D DATA
    if choice == 1:
        input_1d_data()


    # 2D DATA
    elif choice == 2:
        input_2d_data()


    # BUILT-IN FUNCTIONS
    elif choice == 3:
        display_summary()


    # AVERAGE
    elif choice == 4:

        if not data:
            print("\nNo data available.")
        else:
            average = calculate_average(data)
            print("\nAverage value:", round(average, 2))


    # DUPLICATES
    elif choice == 5:
        find_duplicates_menu()


    # RECURSION
    elif choice == 6:
        recursion_menu()


    # FILTER USING LAMBDA
    elif choice == 7:
        lambda_menu()


    # MAP USING LAMBDA
    elif choice == 8:

        if not data:
            print("\nNo data available.")
        else:
            result = double_values(data)

            print("\nOriginal Data:")
            print(data)

            print("\nData after applying lambda with map():")
            print(result)


    # SORT 1D
    elif choice == 9:
        sort_1d_data()


    # SORT 2D
    elif choice == 10:
        sort_2d_data()


    # RETURN MULTIPLE VALUES
    elif choice == 11:

        if not data:
            print("\nNo data available.")
        else:

            minimum, maximum, total, average = dataset_statistics(data)

            print("\n----- Dataset Statistics -----")
            print("Minimum value:", minimum)
            print("Maximum value:", maximum)
            print("Sum of all values:", total)
            print("Average value:", round(average, 2))


    # *args
    elif choice == 12:

        if not data:
            print("\nNo data available.")
        else:
            show_args(*data)


    # **kwargs
    elif choice == 13:

        if not data:
            print("\nNo data available.")
        else:

            show_dataset_info(
                Total_Values=len(data),
                Minimum=min(data),
                Maximum=max(data),
                Sum=sum(data),
                Average=round(calculate_average(data), 2)
            )


    # __doc__
    elif choice == 14:

        print("\n----- Function Documentation -----")

        print("\ndisplay_summary():")
        print(display_summary.__doc__)

        print("\nfactorial():")
        print(factorial.__doc__)

        print("\nfilter_by_threshold():")
        print(filter_by_threshold.__doc__)

        print("\ndataset_statistics():")
        print(dataset_statistics.__doc__)


    # GLOBAL
    elif choice == 15:

        if not data:
            print("\nNo data available.")
        else:
            update_global_summary(data)
            display_global_summary()


    # EXIT
    elif choice == 16:

        print("\nThank you for using the Data Analyzer and Transformer Program.")
        print("Goodbye!")
        break


    else:
        print("\nInvalid choice! Please try again.")
        