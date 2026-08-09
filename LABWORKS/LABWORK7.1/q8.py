'''Develop a program where a UDF accepts *args and filters out the strings from the arguments.
Return a tuple of filtered values (strings in one tuple, numbers in another).'''

def filter_args(*args):
    strings = []
    numbers = []

    for i in args:
        if type(i) == str:
            strings.append(i)
        elif type(i) == int:
            numbers.append(i)

    return tuple(strings), tuple(numbers)

s, n = filter_args("rahul", 10,"python",20,"ai",30)

print("strings:", s)
print("numbers:", n)
# return tuple(strings), tuple(numbers)

# s, n = separate("Rahul", 10, "Python", 20, "AI", 30)

# print("Strings:", s)
# print("Numbers:", n)