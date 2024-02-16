"""
6-7. People: Start with the program you wrote for Exercise 6-1 (page 98). Make
two new dictionaries representing different people, and store all three dictionar-
ies in a list called people. Loop through your list of people. As you loop through
the list, print everything you know about each person.
"""

person1 = {
    "first_name" : "Manu",
    "last_name" : "Rodríguez",
    "age" : 44,
    "city" : "Almería"
}

person2 = {
    "first_name" : "Yolanda",
    "last_name" : "Guirado",
    "age" : 41,
    "city" : "Almería"
}

person3 = {
    "first_name" : "Ainhoa",
    "last_name" : "Rodriguez",
    "age" : 9,
    "city" : "Almería"
} 

people = [person1, person2, person3]

for person in people:
    for key, value in person.items():
        print(f"{key.title()}: {value.title() if isinstance(value, str) else value}")
    print("_______________________________________________________________")

