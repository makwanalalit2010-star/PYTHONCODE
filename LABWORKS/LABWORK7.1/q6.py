'''Write a Python function that accepts an arbitrary number of integer arguments and returns their sum and product.'''

# def calculate(*args):

#     total = 0
#     product = 1

#     for num in args:


#         total += num
#         product *= num

#         return total, product
#     sum,product = calculate(1,2,3,4,5)

#     print("sum:",sum)
#     print("product:",product)

def calculate(*args):

    total = 0
    product = 1

    for i in args:
        total += i
        product *= i

    return total, product

s, p = calculate(2, 3, 4)

print("Sum =", s)
print("Product =", p)

