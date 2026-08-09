'''Q.10 Write a program where a global variable is updated inside a function to keep track of the sum of all numbers entered by the user.'''


total = 0

def add_number(num):
    global total
    total += num

while True:
    num = int(input("enter number (0 to stop): "))
    if num == 0:
        break

    add_number(num)
print("sum of all  numbers entered:", total)