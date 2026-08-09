# Q.4 Write a recursive function to find the sum of all digits of a given number until a single-digit number remains.

def digit_sum(n):

    if n < 10:
        return n

    total = 0

    while n > 0:
        total += n % 10
        n //= 10
        return digit_sum(total)

num = int(input("enter a number: "))
print("result:",digit_sum(num))


