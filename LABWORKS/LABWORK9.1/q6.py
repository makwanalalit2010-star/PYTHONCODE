'''Q.6 Develop a program that uses getter and setter methods to validate the age of a person.

(e.g., age must be greater than 0).'''


class person:
    def __init__(self, age):
        self.__age = age

    def setage(self, age):
        if age > 0:
            self.__age = age
        else:
            print("invalid age")

    def getage(self):
        return self.__age

person1 = person(20)

print("age:", person1.getage())

person1.setage(25)

print("updated age:", person1.getage())

person1.setage(-5)