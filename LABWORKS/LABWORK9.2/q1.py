'''Q.1 Write a program that creates multiple objects of a class and deletes them using the del keyword.'''

class car:
    def __init__(self, brand):
        self.brand = brand
        print(f"{self.brand} car created")

    def __del__(self):
        print(f"{self.brand} car deleted")


car1 = car("bmw")
car2 = car("audi")
car3 = car("suzuki")


del car1
del car2
del car3