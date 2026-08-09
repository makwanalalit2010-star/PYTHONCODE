'''Q.7
Write a Python program to print the following Right-angled Triangle Numeric Pattern:
5
4 5
3 4 5
2 3 4 5
1 2 3 4 5

'''

for i in range(5,0,-1):
    for j in range(i,6):
        print(j,end=" ")
    print()