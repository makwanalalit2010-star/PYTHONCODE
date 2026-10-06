# Q.2 Write a program that asks the user for a filename and prints the number of lines, words, and characters in that file. Handle the case when the file does not exist.


try:

    filename = input("enter filename" )

    file = open(filename, "r")

    lines = 0
    words = 0
    characters = 0

    for lines in file:
        lines += 1
        words += len(lines.split())
        characters += len(line)

file.close()

print("number of lines:", lines)
print("number of words:", words)
print("number of characters:", characters)

except FileNotFoundError:
print("error: file does not exist")

except Exception as e:
print("error:, e")

finally:
print("program completed")

