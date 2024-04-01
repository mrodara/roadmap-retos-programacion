"""
9-1. Restaurant: Make a class called Restaurant. The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message indi-
cating that the restaurant is open.
Make an instance called restaurant from your class. Print the two attri-
butes individually, and then call both methods.
"""

class Restaurant:
    
    def __init__(self, name: str = "", cuisine_type: str = "") -> None:
        self.name = name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"Name: {self.name.title()}")
        print(f"\t Cuisine Type: {self.cuisine_type.title()}")
    
    def open_restaurant(self):
        print(f"Congratulations!!!, The Restaurant {self.name.title()} is open!!!")

restaurant = Restaurant("Tio Pepe", "Bar de Tapas")

print(restaurant.name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()