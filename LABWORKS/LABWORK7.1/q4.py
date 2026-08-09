'''Write a UDF that takes a string as input and returns the frequency of each character in the string as a dictionary.'''

def frequency(s):
    d = {}

    for ch in s:

        if ch in d:
            d[ch] += 1
        else:
            d[ch] = 1

    return d

print(frequency("banana"))