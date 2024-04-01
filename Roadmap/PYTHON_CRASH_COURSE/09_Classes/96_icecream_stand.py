"""
9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand that inherits from the Restaurant class you wrote in
Exercise 9-1 (page 162) or Exercise 9-4 (page 166). Either version of the class
will work; just pick the one you like better. Add an attribute called flavors that
stores a list of ice cream flavors. Write a method that displays these flavors.
Create an instance of IceCreamStand, and call this method.
"""

class Restaurant:
    
    def __init__(self, name: str = "", cuisine_type: str = "") -> None:
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def set_number_served(self, number: int):
        self.number_served = number
    
    def increment_number_served(self, increment:int):
        self.number_served += increment
        
    def describe_restaurant(self):
        print(f"Name: {self.name.title()}")
        print(f"\t Cuisine Type: {self.cuisine_type.title()}")
    
    def open_restaurant(self):
        print(f"Congratulations!!!, The Restaurant {self.name.title()} is open!!!")

class IceCreamStand(Restaurant):
    
    def __init__(self, name: str = "", cuisine_type: str = "", flavors: list = "") -> None:
        super().__init__(name, cuisine_type)
        self.flavors = flavors
    
    def display_flavors(self):
        
        if self.flavors:
            for flavor in self.flavors:
                print(flavor)
        else:
            print("Sorry there not flavors to dispatch")