'''Q.4 Write a program to create a class Book with private attributes title and author.

Add public methods to set and get the attributes.'''


# class book:
#     def __init__(self, title, author):
#         self.__title = title
#         self.__author = author

#     def settitle(self, title):
#         self__title = title

#     def setauthor(self, author):
#         self.__author = author

#     def gettitle(self):
#         return self.__title

#     def gitauthor(self):
#         return self.__author

# book1=book("python programming", "john")

# print("title:", book1.gettitle())
# print("author:", book1.getauthor())

# book1.settitle("advanced python")
# book1.setauthor("david")

# print("updated title:", book1.gettitle())
# print("updated author:", book1.getauthor())

class Book:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    def setTitle(self, title):
        self.__title = title

    def setAuthor(self, author):
        self.__author = author

    def getTitle(self):
        return self.__title

    def getAuthor(self):
        return self.__author


book1 = Book("Python Programming", "John")

print("Title:", book1.getTitle())
print("Author:", book1.getAuthor())

book1.setTitle("Advanced Python")
book1.setAuthor("David")

print("Updated Title:", book1.getTitle())
print("Updated Author:", book1.getAuthor())