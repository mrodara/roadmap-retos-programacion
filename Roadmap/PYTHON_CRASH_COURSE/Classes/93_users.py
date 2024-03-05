"""
9-3. Users: Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.
"""

class User:
    
    def __init__(self, first_name: str = "", last_name: str = "", 
                 age: int = 0, email: str = "") -> None:
        
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
    
    def describe_user(self):
        print(f"{self.first_name.title()} {self.last_name.title()}")
        print(f"\t age: {self.age}")
        print(f"\t email: {self.email.lower()}")
    
    def greet_user(self):
        print(f"Hello {self.first_name.title()} {self.last_name.title()} welcome back!!!")

user = User("ainhoa", "rodriguez", 9, "mjrodriguezarabi@gmail.com")

user.describe_user()
user.greet_user()