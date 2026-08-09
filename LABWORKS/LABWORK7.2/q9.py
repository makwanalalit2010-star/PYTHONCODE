'''Q.9 Create a program that uses a global variable to count the number of times a specific function is called.'''

count = 0

def display():
    global count
    count = count + 1
    print("function called", count, "times")

display()
display()
display()
