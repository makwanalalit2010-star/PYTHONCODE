'''## Level 4: Nested Loops

1. Print pattern:

```
*
**
***
****
*****
```'''


for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()


'''1.Print pattern:
1
12
123
1234'''

for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end="")
    print()


'''*****
   ****
   ***
   **
   *'''

for i in range(5,0,-1):
    for j in range(i):
        print("*",end="")
    print()

'''Print multiplication tables from 1 to 5 (nested loop).'''

for i in range(1,6):
    print("table",i)

    for j in range(1,11):
        print(i,"x",j,"=",i*j)
    print()


'''2.Print all pairs:
(1,1)
(1,2)
(1,3)
...
(3,3)'''

