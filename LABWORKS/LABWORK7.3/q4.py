'''Q.4 Write a program to delete an element by its value from a 1D array.'''

arr=[1,4,456,32,45,76,45,75]

a = int(input("enter the element to remove from array: "))
index=arr.index(a)
del arr[index]
print(arr)

