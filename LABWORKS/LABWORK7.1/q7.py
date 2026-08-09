'''Implement a function that takes a list of student names using *args and prints each name on a new line.'''

def student_names(*args):

    if len(args) == 0:
        print("no names provided")
    else:
        print("student names:")

        for name in args:
            print(name)

student_names("john","jane","james")
student_names()