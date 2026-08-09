'''Q.11 Implement a program to modify a global variable that stores a username.
Use a function to update the name based on user input.'''

username = "admin"

def update_username():
    global username
    username = input("enter new username: ")

print("current username:", username)

update_username()

print("updated username:", username)
