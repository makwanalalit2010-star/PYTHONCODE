'''Q.13 Develop a program to demonstrate the difference between local and global variables with the same name.'''

x = 100

def local_variable():
    x = 50
    print("local variable x:", x)

local_variable()

print("global variable x:", x)