'''Q.1 Create a class Person with attributes such as name and age.

Write a method to display the details. Create multiple objects and call the method for each.'''


# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#         def displayDetails(self):
#             print(f"name: {self.name}")
#             print(f"age: {self.age}")

# person1 = person("harsh", 21)
# person2 = person("renish", 30)

# person1.displayDetails()
# person2.displayDetails()
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def displayDetails(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


person1 = Person("Harsh", 20)
person2 = Person("Rahul", 22)

person1.displayDetails()
person2.displayDetails()