'''Q.5 Create a class Student with appropriate attributes and methods, along with a constructor.'''

class student:
    def __init__(self, name, rollno, marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks

    def displaydetails(self):
        print(f"name: {self.name}")
        print(f"rollno: {self.rollno}")
        print(f"marks: {self.marks}")

    def checkresult(self):
        if self.marks >= 40:
            print("result: pass")
        else:
            print("result: fail")

student1 = student("lalit",1,60)
student1.displaydetails()
student1.checkresult()