# Question: Create a program to demonstrate Hierarchical Inheritance where a base class Animal is inherited by two subclasses Dog and Cat, each having their specific methods.

class animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print("name:", self.name)
        print("age:", self.age)

    def eat(self):
        print(self.name, "is eating")

class dog(animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    