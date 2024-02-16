"""
6-1. Person: Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live. You
should have keys such as first_name, last_name, age, and city. Print each piece
of information stored in your dictionary.
"""
person = {
    "first_name" : "Manu",
    "last_name" : "Rodríguez",
    "age" : 44,
    "city" : "Almería"
}

for key, value in person.items():
    print(f"{key.title()}: {value.title() if isinstance(value, str) else value}")