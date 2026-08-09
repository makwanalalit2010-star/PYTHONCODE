#Q.1 Write a Program to find the length of a 1D array without using any built-in function.

n = int(input("Enter array size: "))

arr = []

for i in range(n):
    x = int(input(f"a[{i}] = "))
    arr.append(x)

count = 0

for i in arr:
    count = count + 1

print("Length of an array: ",count)

#Q.2 Write a Program to find the average of a 1D array without using any built-in function.

n = int(input("Enter array size: "))
arr = []

for i in range(n):
    x = int(input(f"a[{i}] = "))
    arr.append(x)
sum = 0

couunt = 0

for i in arr:
    sum = sum + i
    couunt = couunt + 1

average = sum / couunt

print("Average of an Array:", average)


#Q.3 Write a Program to perform the addition operation of two 1D arrays & store it in another array. (Both array sizes must be the same.)

n = int(input("Enter array size:"))

a = []
b = []
c = []

print("Enter array A elements:")
for i in range(n):
    x = int(input(f"a[{i}] = "))
    a.append(x)

print("Enter array B elements:")
for i in range(n):
    x = int(input(f"b[{i}] = "))
    b.append(x)

for i in range(n):
    c.append(a[i] + b[i])

print("Array C is:", c)

#Q.4 Create an array of numbers from 1 to 10. Multiply each element by 2 and print the result.

arr = [11,12,13,14,15,16,17,18,19,20]

for i in arr:
    print(i * 2)

    
# Q.5 Take user input for a number.
# -Check if it exists in the array.
# -Print the index if found, else print "Not Found".

arr = [10,20,30,40,50]

num = int(input("Enter number: "))

if num in arr:
    print("Index =", arr.index(num))
else:
    print("Not Found")
    

# Q.6 In a user-defined array (by taking input):
# Print all even numbers.
# Print all odd numbers.

n = int(input("Enter array size: "))

arr = []

for i in range(n):
    x = int(input(f"a[{i}] = "))
    arr.append(x)

print("Even Numbers:")
for i in arr:
    if i % 2 == 0:
        print(i)

print("Odd Numbers:")
for i in arr:
    if i % 2 != 0:
        print(i)

# Q.7 In a 1D Array:
# Print the first five elements.
# Print every alternate element.

arr = [10,20,30,40,50,60,70,80]

print("First Five Elements:")
print(arr[0:5])

print("Alternate Elements:")
print(arr[::2])

# Q.8 Print the first, last, and middle elements of the array.

arr = [10,20,30,40,50]
print(arr)
print("First Element:", arr[0])
print("Last Element:", arr[-1])
print("Middle Element:", arr[len(arr)//2])