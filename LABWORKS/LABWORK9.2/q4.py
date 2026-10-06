'''Q.4 Create a class Employee with a default constructor to initialize attributes and a destructor to display a farewell message when the object is deleted.'''

class emp:
    def __init__(self):
        self.name = "abc"
        self.salary = 30000
        print("employee object created")

    def __del__(self):
        print(f"goodbye {self.name}")

employee1 = emp()

print("employee name:", employee1.name)
print("employee salary:", employee1.salary)

del employee1