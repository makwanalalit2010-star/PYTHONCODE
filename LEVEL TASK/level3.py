'''1.Take 3 numbers and print the largest number.'''
num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))
num3 = int(input("enter third number:"))

if num1 > num2:
    if num1 > num3:
        print("num1 is largest number:")
    else:
        print("num3 is largest number:")
else:
    if num2 > num3:
        print("num2 largest number:")
    else:
        print("num3 is largest number:")

'''2.Take a year and check whether it is a leap year.'''

year = int(input("enter a year:"))

if year % 400 == 0:
    if year % 4 == 0:
        print("leap year")
    elif year % 100 == 0:
        print("not leap year")
    else:
        print("not leap year")
else:
    print("not leap year")

'''3. Take username and password:
- If username = "admin"
- Then check password = "1234"
- Print "Login Success" or "Wrong Password"
- Else → "Invalid User"'''

username = input("enter username:")
password = input("enter password:")

if username == "lalit":
    if password == "lalit@123":
        print("login sucess")
    else:
        print("wrong password")
else:
    print("invalid user")

'''1. Take a number and check:
- If even → check if divisible by 4
- Print accordingly'''

num = int(input("enter a number:"))

if num % 2 == 0:
    print(num,"is even")


    if num % 4 == 0:
        print(num,"is divisible by 4")
    else:
        print(num,"is not divisible by 4")
else:
    print(num,"is odd")

'''1. Take temperature:
- 40 → "Very Hot"
- 30–40 → "Hot"
- 20–30 → "Normal"
- < 20 → "Cold"'''

temp = int(input("enter temp:"))

if temp >= 40:
    print("very hot")
elif temp >= 30:
    print("hot")
elif temp >= 20:
    print("normal")
else:
    print("cold")