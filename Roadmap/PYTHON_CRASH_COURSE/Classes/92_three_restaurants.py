"""
9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
different instances from the class, and call describe_restaurant() for each
instance.
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
        
r1 = Restaurant("Casa Sevilla", "cocina mediterranea")
r2 = Restaurant("Entrevinos", "Tapas y Raciones comida tradicional y de vanguardia")
r3 = Restaurant("Virgen del Carmen", "Pescados y Mariscos")

r1.describe_restaurant()
r1.open_restaurant()
r2.describe_restaurant()
r2.open_restaurant()
r3.describe_restaurant()
r3.open_restaurant()
 