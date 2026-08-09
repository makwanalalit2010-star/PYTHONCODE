'''1Take a number and check if it is positive, negative, or zero.'''

num = int(input("enter a number:"))

if num > 0:
    print("positive number")
elif num < 0:
    print("negetive number")
else:
    print("zero")


    '''2. Take age as input and check:
    - If age ≥ 18 → print "Eligible to vote"
    - Else → "Not eligible'''

age = 18
    
if age >= 18:
 print("eligible to vote")

else:
 print("not eligible")
 

 '''3.Take a number and check if it is divisible by 5 or not.'''

num = int(input("enter a number:"))

if num % 5 == 0:
    print("number divisible by 5")
else:
    print("number not divisible by 5")

'''Take two numbers and print which one is greater.'''

num = 23
num1 = 40

if num > num1:
    print(num,"is greater")
elif num1 > num:
    print(num1,"is greater")
else:
    print("both equal")
    
'''5. Take marks and print:
- ≥ 90 → Grade A
- ≥ 75 → Grade B
- ≥ 50 → Grade C
- Else → Fail'''

marks = int(input("enter marks:"))
 

if marks >= 90:
  print(" grade A")
elif marks >= 75:
  print(" grade B")
elif marks >= 50:
  print(" grade C")
else:
  print("fail")
  