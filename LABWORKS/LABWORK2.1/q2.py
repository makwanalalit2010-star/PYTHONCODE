'''Create a program that:

Accepts a user's age as input.

Uses nested 'if-else statements to categorize the user into age groups:

Child (0-12)

Teenager (13-19)

Adult (20-59)

Senior (60+'''

age = int(input("enter your age:"))
if age >= 0:
    if age <= 12:
        print("child")
    else:
        if age <= 19:
            print("teenager")
        else:
            if age <= 59:
                print("adult")
            else:   
             print("senior")
else:
        print("invalid age")   
