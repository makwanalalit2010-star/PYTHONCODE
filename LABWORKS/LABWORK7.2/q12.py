'''Q.12 Write a program with two functions:
One function initializes a global variable and another increments it by a user-defined value.'''

# count = 0

# def initialize_count():
#     global count
#     count = 100
# def increment_count():
#     global count
#     value = int(input("enter value to add: "))
#     count += value

#     initialize_count()

#     print("initial count =", count)

#     increment_count()

#     print("updated count =", count)

count = 0

def initialize():
    global count
    count = 100

def increment():
    global count
    value = int(input("Enter value to add: "))
    count += value

initialize()

print("Initial Count =", count)

increment()

print("Updated Count =", count)