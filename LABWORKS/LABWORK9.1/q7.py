# Q.7 Create a class Student with private attributes for name and marks (of three subjects).

# Add a method to calculate and display the average. Add public methods to calculate and display the grade based on marks.
class student:
    def __init__(self, name, python, java, dbms):
        self.__name = name
        self.__python = python
        self.__java = java
        self.__dbms = dbms

        def calculateaverage(self):
            average = (self.__python + self.__java + self.__dbms) / 3
            print(f"average: {average}")

        def displaygrade(self):
            average = (self.__python + self.__java + self.__dbms) / 3

            if average >= 90:
                grade ="A+"
            elif average >= 80:
                grade ="A"
            elif average >= 70:
                grade ="B"
            elif average >= 60:
                grade ="C"
            elif average >= 40:
                grade = "D"
            else:
                grade = "fail"

            print(f"grade: {grade}")

student1 = student("harsh", 80, 75, 90)

student1.calculateaverage()
student1.displaygrade()