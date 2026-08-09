'''Q.6 Create a lambda function to calculate the square of a number.
Use it inside a map() function to generate a list of squares from a given list of numbers.'''

numbers = [1,2,3,4,5]

square = list(map(lambda a: a**2,numbers))

print("square:",square)

