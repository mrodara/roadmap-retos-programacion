"""
6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
Think of five names, and use them as keys in your dictionary. Think of a favorite number for each person, 
and store each as a value in your dictionary. 
Print each person’s name and their favorite number. For even more fun, poll a few
friends and get some actual data for your program.
"""

favorite_numbers = {
    "Ainhoa" : 24,
    "Alma" : 29,
    "Yolanda" : 9,
    "Manu" : 16
}

for key, value in favorite_numbers.items():
    print(f"The {key.title()}`s favorite number is: {value}")