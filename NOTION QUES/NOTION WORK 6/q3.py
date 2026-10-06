# Q.3 Create a simple bank balance program. User can deposit or withdraw money. Handle exceptions for negative amounts and insufficient balance

balance = 1000

try:
    print("1.deposit")
    print("2. withdraw")


    choice = int(input("enter your choice: "))
    amount = float(input("enter amount:"))

    if amount < 0:
        raise ValueError("amount cannot be negative")

    if choice == 1:
        balance = balance + amount
        print("amount deposited successfully")
        print("current balance:", balance)

    elif choice == 2:

        if amount > balance:
            raise Exception("insufficient balance")

        balance = balance - amount
        print("amount withfrawn successfully")
        print("current balance:", balance)

    else:
        raise ValueError("invalid choice")

except ValueError as e:
    print("error:", e)

except Exception as e:
    print("error:", e)

finally:
    print("banking program completed")