'''Develop a program to calculate the sum of all elements in a 2D array separately.

'''

arr = [
    [1,2,3],
    [4,5,6]
]

total = 0

for i in range(2):
    for j in range(3):
        total = total + arr[i][j]

print("sum of all element:", total)