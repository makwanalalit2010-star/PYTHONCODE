'''Write a function that accepts **kwargs to print a formatted description of a person.'''

def person(**kwargs):

    print("name:", kwargs["name"])
    print("age:", kwargs["age"])
    print("city:",kwargs["city"])

person(name="lalit", age=21, city="ahmedabad")