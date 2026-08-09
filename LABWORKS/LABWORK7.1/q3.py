'''Implement a program where a UDF accepts a list of integers and returns the square of each integer in a new list using list comprehension.'''

# def square_list(int_list):

#     return [i**2 for i in int_list]

# numbers = [1,2,3,4,5]

# squared_numbers = square_list(numbers)

# print("Original numbers:", numbers)
# print("squared numbers:", squared_numbers)


def square_list(lst):

    return [i**2 for i in lst]

numbers = [1,2,3,4,5]

result = square_list(numbers)

print(result)
