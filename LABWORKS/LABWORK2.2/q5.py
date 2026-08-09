'''Write a Program in Python to create a menu-driven fast-food order system using the 'match case' feature.
For example:
Press I to order a Sandwich
Press 2 to order a Pizza
Press 3 to order a Burger
Extend this program by adding a nested match case for each menu item's
subtype selection by the user.
For example:
Press 1 for Thin Crust Pizza
Press 2 for Cheese Burst Pizza
Press 3 for Fresh Dough Pizza'''

print("press 1 for sandwich")
print("press 2 for pizza")
print("press 3 for burger")

choice = int(input("enter your choice:"))

case 1:
print("sandwich menu:")
print("press 1 for veg sandwich")
print("press 2 for grilled sandwitch")
print("press 3 for cheese sandwich")

sub = int(input(enter your choice:))

match sub:
    case1:
print("your ordered veg sandwich:")
    case2:
print("your ordered grilled sandwich:")
    case3:
print("your ordered cheese sandwich:")
    case_:
print("invalid sandwich choice!")

case