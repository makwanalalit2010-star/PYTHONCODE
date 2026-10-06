'''Implement a program to sort a list of tuples based on the second element of each tuple using the sorted() function.

'''

data = [(1,50), (2,20), (3,40), (4,10)]

result = sorted(data, key=lambda x: x[1])

print("sorted list:", result)