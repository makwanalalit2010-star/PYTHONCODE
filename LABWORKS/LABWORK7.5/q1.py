'''Implement a program to create a 2D array (list of lists) representing a 3x3 matrix. Display the matrix in a tabular format.'''
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for row in matrix:
    for element in row:
        print(element, end =" ")
    print()