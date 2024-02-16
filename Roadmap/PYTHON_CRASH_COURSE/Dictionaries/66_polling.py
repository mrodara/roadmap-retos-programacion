"""
6-6. Polling: Use the code in favorite_languages.py (page 96).
•Make a list of people who should take the favorite languages poll. Include
some names that are already in the dictionary and some that are not.
•Loop through the list of people who should take the poll. If they have
already taken the poll, print a message thanking them for responding.
If they have not yet taken the poll, print a message inviting them to take
the poll.
"""

favorite_numbers = {
    "Ainhoa" : 24,
    "Alma" : 29,
    "Yolanda" : 9,
    "Manu" : 16
}

people = ["ainhoa", "alma", "yolanda", "coco", "bella"]

for person in people:
    if person.title() in favorite_numbers.keys():
        print(f"Hello {person.title()} thanks for responding the polling")
    else:
        print(f"What`s up {person.title()}, respond our poll about your favorite number")


#print(people[0] in favorite_numbers.keys())