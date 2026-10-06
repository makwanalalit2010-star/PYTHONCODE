# # Implement a program to demonstrate method overriding where a class Animal has a method speak(), and subclasses Dog and Cat override it with their respective sounds.

# class animal:
#     def speak(self):
#         print("animal makes a sound")

# class dog(animal):
#     def speak(self):
#         print("dog says: woof woof")

# class cat(animal):
#     def speak(self):

        
"""
Employee Management System - OOP Project
Demonstrates: Classes, Encapsulation, Inheritance, Method Overriding,
Method Overloading (via multiple constructors), super(), issubclass(), Destructor
"""

from typing import Optional, List


# ============================================================
# Base Class: Employee
# ============================================================
class Employee:
    """
    Base class representing an Employee.
    Encapsulates sensitive data (employee_id, salary) as private attributes.
    """

    def __init__(
        self,
        name: str = "Unknown",
        age: int = 0,
        employee_id: str = "N/A",
        salary: float = 0.0
    ):
        """
        Constructor with default arguments to support multiple ways of
        creating Employee objects (method overloading simulation).
        """
        self.name = name
        self.age = age
        self.__employee_id = employee_id          # private
        self.__salary = float(salary)             # private
        print(f"Employee object created for: {self.name}")

    # ---------- Getters ----------
    def get_employee_id(self) -> str:
        """Getter for private employee_id."""
        return self.__employee_id

    def get_salary(self) -> float:
        """Getter for private salary."""
        return self.__salary

    # ---------- Setters ----------
    def set_employee_id(self, employee_id: str) -> None:
        """Setter for private employee_id."""
        if employee_id and str(employee_id).strip():
            self.__employee_id = str(employee_id).strip()
        else:
            print("Invalid Employee ID. Keeping previous value.")

    def set_salary(self, salary: float) -> None:
        """Setter for private salary with basic validation."""
        try:
            salary = float(salary)
            if salary >= 0:
                self.__salary = salary
            else:
                print("Salary cannot be negative. Keeping previous value.")
        except (ValueError, TypeError):
            print("Invalid salary value. Keeping previous value.")

    # ---------- Display Method ----------
    def display(self) -> None:
        """Display basic employee details. Can be overridden by subclasses."""
        print("\nEmployee Details:")
        print(f"Name        : {self.name}")
        print(f"Age         : {self.age}")
        print(f"Employee ID : {self.get_employee_id()}")
        print(f"Salary      : ${self.get_salary():.1f}")

    # ---------- Destructor ----------
    def __del__(self):
        """Destructor to clean up resources when object is destroyed."""
        pass  # Resources cleaned when object is deleted


# ============================================================
# Derived Class: Manager
# ============================================================
class Manager(Employee):
    """
    Manager inherits from Employee.
    Adds department attribute and overrides display().
    """

    def __init__(
        self,
        name: str = "Unknown",
        age: int = 0,
        employee_id: str = "N/A",
        salary: float = 0.0,
        department: str = "General"
    ):
        # Call parent constructor using super()
        super().__init__(name, age, employee_id, salary)
        self.department = department
        print(f"Manager object created for: {self.name}")

    def display(self) -> None:
        """Override display() to include department information."""
        print("\nManager Details:")
        print(f"Name        : {self.name}")
        print(f"Age         : {self.age}")
        print(f"Employee ID : {self.get_employee_id()}")
        print(f"Salary      : ${self.get_salary():.1f}")
        print(f"Department  : {self.department}")


# ============================================================
# Derived Class: Developer
# ============================================================
class Developer(Employee):
    """
    Developer inherits from Employee.
    Adds programming_language attribute and overrides display().
    """

    def __init__(
        self,
        name: str = "Unknown",
        age: int = 0,
        employee_id: str = "N/A",
        salary: float = 0.0,
        programming_language: str = "Python"
    ):
        # Call parent constructor using super()
        super().__init__(name, age, employee_id, salary)
        self.programming_language = programming_language
        print(f"Developer object created for: {self.name}")

    def display(self) -> None:
        """Override display() to include programming language information."""
        print("\nDeveloper Details:")
        print(f"Name                 : {self.name}")
        print(f"Age                  : {self.age}")
        print(f"Employee ID          : {self.get_employee_id()}")
        print(f"Salary               : ${self.get_salary():.1f}")
        print(f"Programming Language : {self.programming_language}")


# ============================================================
# Helper: Simple Person (for menu option 1 – matches sample UI)
# ============================================================
class Person:
    """
    Lightweight Person class used for the 'Create a Person' menu option
    shown in the project sample console interaction.
    """

    def __init__(self, name: str = "Unknown", age: int = 0):
        self.name = name
        self.age = age

    def display(self) -> None:
        print("\nPerson Details:")
        print(f"Name : {self.name}")
        print(f"Age  : {self.age}")


# ============================================================
# Main Application / Menu-Driven UI
# ============================================================
def demonstrate_issubclass() -> None:
    """Show issubclass() usage as required by the project."""
    print("\n--- issubclass() Demonstration ---")
    print(f"issubclass(Manager, Employee)   : {issubclass(Manager, Employee)}")
    print(f"issubclass(Developer, Employee) : {issubclass(Developer, Employee)}")
    print(f"issubclass(Employee, Manager)   : {issubclass(Employee, Manager)}")
    print(f"issubclass(Manager, object)     : {issubclass(Manager, object)}")


def main() -> None:
    print("--- Python OOP Project: Employee Management System ---")

    # Storage for created objects
    persons: List[Person] = []
    employees: List[Employee] = []   # holds Employee, Manager, Developer
    managers: List[Manager] = []
    developers: List[Developer] = []

    while True:
        print("\nChoose an operation:")
        print("1. Create a Person")
        print("2. Create an Employee")
        print("3. Create a Manager")
        print("4. Create a Developer")
        print("5. Show Details")
        print("6. Demonstrate issubclass()")
        print("7. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            # Create a Person
            name = input("Enter Name: ").strip() or "Unknown"
            try:
                age = int(input("Enter Age: ").strip() or "0")
            except ValueError:
                age = 0
                print("Invalid age. Using 0.")

            person = Person(name, age)
            persons.append(person)
            print(f"\nPerson created with name: {name} and age: {age}.")

        elif choice == "2":
            # Create an Employee
            name = input("Enter Name: ").strip() or "Unknown"
            try:
                age = int(input("Enter Age: ").strip() or "0")
            except ValueError:
                age = 0
                print("Invalid age. Using 0.")
            emp_id = input("Enter Employee ID: ").strip() or "N/A"
            try:
                salary = float(input("Enter Salary: ").strip() or "0")
            except ValueError:
                salary = 0.0
                print("Invalid salary. Using 0.0.")

            emp = Employee(name, age, emp_id, salary)
            employees.append(emp)
            print(
                f"\nEmployee created with name: {name}, age: {age}, "
                f"ID: {emp_id}, and salary: ${salary:.1f}."
            )

        elif choice == "3":
            # Create a Manager
            name = input("Enter Name: ").strip() or "Unknown"
            try:
                age = int(input("Enter Age: ").strip() or "0")
            except ValueError:
                age = 0
                print("Invalid age. Using 0.")
            emp_id = input("Enter Employee ID: ").strip() or "N/A"
            try:
                salary = float(input("Enter Salary: ").strip() or "0")
            except ValueError:
                salary = 0.0
                print("Invalid salary. Using 0.0.")
            department = input("Enter Department: ").strip() or "General"

            mgr = Manager(name, age, emp_id, salary, department)
            managers.append(mgr)
            employees.append(mgr)  # also store in general list for polymorphism
            print(
                f"\nManager created with name: {name}, age: {age}, "
                f"ID: {emp_id}, salary: ${salary:.1f}, and department: {department}."
            )

        elif choice == "4":
            # Create a Developer
            name = input("Enter Name: ").strip() or "Unknown"
            try:
                age = int(input("Enter Age: ").strip() or "0")
            except ValueError:
                age = 0
                print("Invalid age. Using 0.")
            emp_id = input("Enter Employee ID: ").strip() or "N/A"
            try:
                salary = float(input("Enter Salary: ").strip() or "0")
            except ValueError:
                salary = 0.0
                print("Invalid salary. Using 0.0.")
            lang = input("Enter Programming Language: ").strip() or "Python"

            dev = Developer(name, age, emp_id, salary, lang)
            developers.append(dev)
            employees.append(dev)
            print(
                f"\nDeveloper created with name: {name}, age: {age}, "
                f"ID: {emp_id}, salary: ${salary:.1f}, and language: {lang}."
            )

        elif choice == "5":
            # Show Details
            print("\nChoose details to show:")
            print("1. Person")
            print("2. Employee")
            print("3. Manager")
            print("4. Developer")
            sub = input("Enter your choice: ").strip()

            if sub == "1":
                if not persons:
                    print("No Person records found.")
                else:
                    for p in persons:
                        p.display()
            elif sub == "2":
                # Show pure Employee objects (exclude Manager/Developer)
                pure_emps = [e for e in employees if type(e) is Employee]
                if not pure_emps:
                    print("No Employee records found.")
                else:
                    for e in pure_emps:
                        e.display()
            elif sub == "3":
                if not managers:
                    print("No Manager records found.")
                else:
                    for m in managers:
                        m.display()
            elif sub == "4":
                if not developers:
                    print("No Developer records found.")
                else:
                    for d in developers:
                        d.display()
            else:
                print("Invalid choice.")

        elif choice == "6":
            demonstrate_issubclass()

        elif choice == "7":
            print("\nExiting the system. All resources have been freed.")
            print("Goodbye!")
            # Explicitly clear lists so destructors can run
            persons.clear()
            employees.clear()
            managers.clear()
            developers.clear()
            break

        else:
            print("Invalid choice. Please try again.")

        print("\n--- Choose another operation ---")


if __name__ == "__main__":
    main()