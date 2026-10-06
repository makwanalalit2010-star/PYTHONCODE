'''Write a program to transpose a 2x3 matrix and display its transpose (3x2 matrix).'''

matrix = [
    [1,2,3],
    [4,5,6]
]

transpose = []

for j in range(3):
    row = []
    for i in range(2):
        row.append(matrix[i][j])
        transpose.append(row)

print("original matrix:")
for row in matrix:
    print(row)

print("transpose matrix:")
for row in transpose:
    print(row)