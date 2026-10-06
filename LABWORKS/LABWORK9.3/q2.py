'''Question: Implement a program to demonstrate Multiple Inheritance using classes Teacher and Administrator inherited by a class Headmaster.'''


class teacher:
    def teach(self):
        print("teacher teaches students")

class administrator:
    def manage(self):
        print("administrator manages school")

class headmanster(teacher, administrator):
    pass

obj = headmanster()

obj.teach()
obj.manage()