data = []
dataset_summary = {}
#input data
lst = []

def inputArray(lst):
    userInput = int(input("Enter type of Array: "))
    match userInput:
        case 1:

            lst = list(map(int,input("Enter the value by space: ").split()))
            return lst


        case 2:

            rows = int(input("Enter number of rows: "))
            cols = int(input("Enter number of columns: "))

            values = rows * cols
            for i in range(rows):
                lsts = list(map(int,input(f"Ente the value {values} by space: ").split(" ")))
                lst.append(lsts)
            return lst
            
lst = inputArray(lst)

print(lst)

#data summary
def dataSummary(lst):
    
    singlelist = []

    if isinstance(lst[0], list):

     for row in lst:
        singlelist.extend(row)

    else:
        singlelist = lst

    return f'''
    Data Summary:
    - Total Element: {len(singlelist)}
    - Minimum value: {min(singlelist)}
    - Maximum value: {max(singlelist)}
    - Sum of all Value: {sum(singlelist)}
    - Average value: {sum(singlelist) / len(singlelist)}
    '''
print(dataSummary(lst))

def calculateaverage(data):

    singlelist = []

    if not isinstance(data[0], list):

        singlelist = data

    else:

        for row in data:
            singlelist.extend(row)
    return sum(singlelist) / len(singlelist)


def showvalues(*args):

    print("\nvalues using *args:")

    for value in args:
        print(value, end=" ")

        print()
def showcharacteristics(**kwargs):

    print("\n dataset characteristics:")

    for key, value in kwargs.items():
        print("-", key, ":", value)

    def recursion(n):
        if n == 0 or n == 1:
            return 1
        return n * factorial(n - 1)

#

# def input_data():
#      global data

#      print("\n data input")
#      print("1. enter 1D array")
#      print("2. enter 2D array")

# choice = int(input("enter your choice: "))

# if choice == 1:
#      values = input("enter data for a 1D array (seprated by spaces):")

#      data = list(map(int, values.split()))

#      print("data has been stored successfully!")
#      print("data:", data)

# elif choice == 2:
#      rows = int(input("enter numbers of rows: "))
#      cols = int(input("enter number of columns: "))


# data = []

# for i in range(rows):


#      row = list(
#           map(
#                int,
#                input(
#                     f"enter values for row {i + 1} "
#                     f"(seprated by spaces): "
#                ).split()
#           )
#      )

# while len(row) != cols:
#      print("please enter exactly", cols, "values.")
#      row = list(
#           map(
#                int,
#                input(
#                     f"enter values for row {i + 1}: "
#                ).split()
#           )
#      )          
#      data.append(row)

#      print("\n 2D data has been stored suceesfully!")
# else:
#      print("invalid choice!")
# while True:

#     print("welcome to the data analyzer and transformer")



#     print("\nMain Menu")
#     print("1. Input Data")
#     print("2. Display Data Summary (Built-in Functions)")
#     print("3. Calculate Factorial (Recursion)")
#     print("4. Filter Data by Threshold (Lambda Function)")
#     print("5. Sort Data")
#     print("6. Display Dataset Statistics (Return Multiple Values)")
#     print("7. Exit Program")

#     choice = int(input("\nPlease enter your choice: "))

#     if choice == 1:

#         print("\n choose data type")
#         print("1. 1D array")
#         print("2. 2D array")

#         data_choice = int(input("enter your choice:"))

#         if data_choice == 1:

