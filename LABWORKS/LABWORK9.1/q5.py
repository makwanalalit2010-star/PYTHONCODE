'''Q.5 Implement a class Account with a private attribute balance.

Create methods to deposit and withdraw money. Add a method to display the balance. Ensure balance cannot be accessed directly.'''

# class amount:
#     def __init__(self):
#         self.__balance = 0 

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance = amount + 1
#             print("amount deposit successfully")
#         else:
#             print("invalid amount")

#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance = amount
#             print("amount withdrawn successfully")
#         else:
#             print("insufficient balance")

#     def displaybalance(self):
#         print(f"balce: {self.__balance}")

# account1 = account()

# account1.deposit(5000)
# account1.displaybalance()

# account1.withdraw(2000)
# account1.displaybalance()

class Account:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount Deposited Successfully")
        else:
            print("Invalid Amount")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Amount Withdrawn Successfully")
        else:
            print("Insufficient Balance")

    def displayBalance(self):
        print(f"Balance: {self.__balance}")


account1 = Account()

account1.deposit(5000)
account1.displayBalance()

account1.withdraw(2000)
account1.displayBalance()