'''Check numbers from 1 to 50 and print whether they are divisible by 2, 3, or both.'''
for i in range(1,51):
    if i % 2 == 0 and i % 3 == 0:
        print(i,"divisible by both")

    elif i % 2 == 0:
        print(i,"divisible by 2")


    elif i % 3 == 0:
        print(i,"divisible by 3")

    else:
        print(i,"not divisible by 2 or 3")