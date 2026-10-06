# Q.1 Write a program to create a file marks.txt and write marks of 5 students. Then read and display the average marks.

try:

    file = open("mark.txt", "w")

    for i in range(1, 6):
        marks = float(f"enter marks of student {i}: ")

        if marks < 0 or marks > 100:
            raise ValueError("marks must be betwwen o and 100")

        file.write(str(marks) + "\n")

    file.close()

    file = open("marks.txt", "r")

    total = 0
    count = 0

    for line in file:
        total += float(line)
        count += 1

        file.close()

        average = total / count

        print("average marks:", average)

except ValueError as e:
    print("error:", e)

except FileNotFoundError:
    print("error: file not found")

except Exception as e:
    print("error:", e)

finally:
    print("program completed")

