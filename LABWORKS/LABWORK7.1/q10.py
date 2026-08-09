'''Implement a function that accepts product details like name, price and quantity using **kwargs.
Return total cost.'''

def product(**kwargs):

   total_cost = kwargs["price"] * kwargs["quantity"]

   print("product name:",kwargs["name"])
   print("price:",kwargs["price"])
   print("quantity:",kwargs["quantity"])
   print("total cost:",total_cost)

product(name = "mobile", price = 10000, quantity = 2)

