'''Q.7 Write a program to filter out odd numbers from a list using a lambda function and the filter() method.'''

numbers = [1,2,3,4,5,6,7,8,9,10]

odd_numbers = list(filter(lambda b: b % 2 != 0, numbers))

print("odd numbers:", odd_numbers)