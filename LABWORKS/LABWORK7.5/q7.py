'''Develop a program to sort a list of dictionaries by a specific key using the sorted() function.

'''

students = [
    {"name": "harsh", "marks": 75},
    {"name": "rahul", "marks": 90},
    {"name": "kiran", "marks": 65},
    {"name": "amit", "marks": 85}
]

result = sorted(students, key=lambda x: x["marks"])

print("sorted list:")
for student in result:
    print(student)