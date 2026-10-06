# Question: Write a program that opens a file, handles any exceptions if the file doesn’t exist, and ensures the file is closed using the finally block.

file = None

try:

    filename = input("enter filename: ")

    file = open(filename, 'r')

    content = file.read()

    print("file content:")
    print(content)

except FileNotFoundError:
    print("error: file not found.")

except Exception as e:
    print("error:", e)

finally:
    if file is not None:
        file.close()

        print("file closed.")