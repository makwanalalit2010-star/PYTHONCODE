'''1.Print numbers from 1 to 10 using loop.'''

for i in range(1,11):
    print(i)

'''2. Print numbers from **10 to 1 (reverse order)'''

for i in range(10,0,-1):
    print(i)

'''3. Take a number and print its **multiplication table**.'''

num = 5

for i in range(1,11):
    print(num,"x",i,"=",num * i)

'''4. Take a number and calculate **sum from 1 to n**.'''

num = int(input("enter a number:"))
sum = 0

for i in range(1,num + 1):
   sum = sum + i
   print("sum =",sum)

'''5. Take a number and count how many **digits** it has.'''

a = int(input("enter a number:"))

count = 0

while a > 0:
   a = a // 10
   count = count + 1

print("number of digits =",count)

