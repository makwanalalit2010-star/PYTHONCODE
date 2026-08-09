'''Q.14 Write a function that takes a list of integers and returns the sum, maximum, and minimum values as separate results.'''

def calculate(numbers):
    total_sum = sum(numbers)
    maximum = max(numbers)
    minimum = min(numbers)

    return total_sum, maximum, minimum

lst = [10,20,30,40,50]

result_sum, result_max, result_min = calculate(lst)

print("sum: ", result_sum)
print("maximum: ", result_max)
print("minimum: ", result_min)
