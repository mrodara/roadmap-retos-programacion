"""
6-5. Rivers: Make a dictionary containing three major rivers and the country
each river runs through. One key-value pair might be 'nile': 'egypt'.
•Use a loop to print a sentence about each river, such as The Nile runs
through Egypt.
•Use a loop to print the name of each river included in the dictionary.
•Use a loop to print the name of each country included in the dictionary.
"""

rivers = {
    "guadalquivir": "sevilla",
    "ebro": "zaragoza",
    "andarax": "almeria",
    "amazonas": "brasil",
    "nilo": "egipto",
    "sena": "paris"
}

#First loop
for key, value in rivers.items():
    print(f"The {key.title()}`s runs through {value.title()}")
    
#Second loop
for key in rivers.keys():
    print(key.upper())

#Third loop
for value in rivers.values():
    print(value.title())