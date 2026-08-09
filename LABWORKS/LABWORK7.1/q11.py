'''Develop a program that allows users to pass any combination of attributes for an employee using **kwargs.'''

# def employee(**kwargs):

#     print("Employee details:")
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

#     employee(
#         name="raj",
#         age = 21,
#         designation = "developer",
#         experience = 2
#     )

def employee(**kwargs):

    print("Employee Information")

    for key, value in kwargs.items():
        print(f"{key} : {value}")

employee(
    name="Raj",
    age=28,
    designation="Software Engineer",
    experience=5
)