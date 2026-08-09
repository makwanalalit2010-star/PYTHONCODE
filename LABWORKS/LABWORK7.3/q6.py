'''Q.6 Implement a program to search for an element in a 1D array and return its index.'''

# def findind(l):
#     """
#     Searches a list for a user-specified integer.
#     Parameters:
#     l (list): The list to search.
#     Returns:
#     int: The index of the element, or a message if not found.
#     """
#     a = int(input("Enter the element to search: "))
#     for i in range(len(l)):  
#         if a == l[i]:       
#             return i
#     return "element not found"                
# arr = [1, 4, 456, 32, 45, 76, 45, 75]
# print(findind(arr))

arr = [10, 20, 30, 40, 50]

x = 50

index = arr.index(x)

print("Index =", index)