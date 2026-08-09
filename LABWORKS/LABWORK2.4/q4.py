'''Q.4
Write a Python program to print multiplication tables using nested loops for up to N numbers in this format:
1 x 1 = 1
1 x 2 = 2
…

Where N is the user-given number.

'''

num = int(input("enter the num:"))

for i in range(1, num + 1):
    for j in range(1,11):
        print(i,"x",j,"=",i*j)