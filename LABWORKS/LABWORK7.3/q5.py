'''Q.5 Develop a program to update an element in a 1D array based on its index.'''

arr=[1,4,456,32,45,76,45,75]

print(arr)
a=int(input("enter the number to update: "))
b=int(input("enter the new number: "))
c=arr.index(a)
arr[c] = b
print(arr)