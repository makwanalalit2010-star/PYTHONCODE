'''Q.5 Create a recursive function to print all prime numbers between two given numbers.'''

# def is_prime(num, i=2):

#     if num < 2:
#         return False

#         if i * i > num:
# return True
# if num % i == 0:
#      return False
# return is_prime(num, i + 1)

# def print_primes(start, end):

#      if start > end:
#         return
#      if is_prime(start):
#           print(start)
#           print_primes(start + 1, end)

#           a = int(input("enter start: "))
#           b = int(input("enter end: "))

# print("prime numbers are:")
# print_primes(a, b)
        
def is_prime(num, i=2):
    if num < 2:
        return False
    if i * i > num:
        return True
    if num % i == 0:
        return False
    return is_prime(num, i + 1)

def print_primes(start, end):
    if start > end:
        return
    if is_prime(start):
        print(start)
    print_primes(start + 1, end)

a = int(input("Enter start: "))
b = int(input("Enter end: "))

print("Prime Numbers are:")
print_primes(a, b)