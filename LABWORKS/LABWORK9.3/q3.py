# '''Question: Write a program to demonstrate Multilevel Inheritance using a class hierarchy:
# Grandparent → Parent → Child
# Each class should have a method to display its role.


class grandparent:
    def display_grandparent(self):
        print("i am grandparent")

class parent(grandparent):
    def display_parent(self):
        print("i am parent")

class child(parent):
    def display_child(self):
        print("i am child")

obj = child()

obj.display_grandparent()
obj.display_parent()
obj.display_child()