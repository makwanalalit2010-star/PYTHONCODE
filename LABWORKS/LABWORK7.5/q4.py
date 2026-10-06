'''Write a program to find the maximum and minimum values in a 2D array.

'''

arr = [
    [10,25,5],
    [40,15,30]
]

maximum = arr[0][0]
minimum = arr[0][0]

for i in range(2):
    for j in range(3):
        if arr[i][j] > maximum:
            maximum = arr[i][j]

        if arr[i][j] < minimum:
            minimum = arr[i][j]
print("maximum value:", maximum)
print("minimum value:", minimum)