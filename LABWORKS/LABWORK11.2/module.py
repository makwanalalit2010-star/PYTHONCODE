# celsius = [0, 10,20, 30, 40]
# fahrenheit = []

# for c in celsius:
#     f = (c * 9/5) + 32
#     fahrenheit.append(f)

#     print(fahrenheit)

# celsius = [0, 10, 20, 30, 40]

# fahrenheit = [c * 9/5 + 32 for c in  celsius]

# print(fahrenheit)

# using lambda:

# celsius = [0, 10, 20, 30, 40]

# fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))

# print(fahrenheit)



# num = [12,5,8,23,4,42,7]

# def is_even(n):
#     return n % 2 == 0

# even_num = list(filter(is_even, num))

# result = list(filter(is_even, num))

# result = sorted(even_num, reverse=True)

# print(result)




# numbers = [12,5,8,23,16,4,42,7]

# max_num = numbers[0]

# for num in numbers:
#     if num > max_num:
#         max_num = num

#         print(max_num)


# from functools import reduce

# numbers = [12,5,8,23,16,4,42,7]

# numbers.sort()

# max_num = numbers[-1]

# print(max_num)



# numbers = [12,5,8,23,16,4,42,7]
# maximum = numbers[0]

# for num in numbers:
#     if num > maximum:
#         maximum = num
# print(maximum)


# from functools import reduce

# numbers = [12,5,8,23,16,4,42,7]

# max_num = reduce(lambda a, b: a if a > b else b, numbers)
# print(max_num)


from functools import reduce

words = ["python", "is", "awesome", "and", "powerful"]

filtered = list(filter(lambda word: len(word) > 3, words))
print(filtered)

uppercase = list(map(lambda word: word.upper(), filtered))
print(uppercase)

sorted_words = sorted(uppercase)
print(sorted_words)