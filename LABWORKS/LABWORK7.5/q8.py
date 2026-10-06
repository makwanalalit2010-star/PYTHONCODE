'''Write a program to demonstrate the difference between sort() (in-place) and sorted() (returns a new list) using a sample list.

'''

numbers = [50,20,40,10,30]

a = numbers.copy()
a.sort()

print("original list after sort():", a)

b = [50,20,40,10,30]
result = sorted(b)

print("original list after sorted():", b)
print("new sorted list:", result)