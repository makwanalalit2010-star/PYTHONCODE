'''Q.8
Write a Python program to print the following Right-angled Triangle Numeric Pattern:
1 2 3 4 5
2 3 4 5
3 4 5
4 5
5

'''

for i in range(1, 6):
    for j in range(i, 6):
        print(j, end=" ")
    print()