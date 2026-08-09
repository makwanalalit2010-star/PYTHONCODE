'''Create a function that calculates the area of a rectangle.
Add a_doc_string to describe the function's purpose, parameters, and return type.
Write code to print the doc string.'''

def rectangle_area(length,width):

    return length * width

area = rectangle_area(5,10)

print("area of rectangle:",area)

print("\nDoc string:")
print(rectangle_area.__doc__)