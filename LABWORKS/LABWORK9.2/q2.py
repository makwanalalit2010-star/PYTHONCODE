'''Q.2 Create a class Animal with a constructor that initializes the name attribute.
Add a method to display the name of the animal.'''

class animal:
    def __init__(self, name):
        self.name = name

    def displayname(self):
        print(f"animal name: {self.name}")

animal1 = animal("lion")
animal2 = animal("tiger")


animal1.displayname()
animal2.displayname()