import json

# JSON
person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScript", "React", "Python"]
}'''

# let's change JSON to dictionary
person_dct = json.loads(person_json)
#print(type(person_dct))
#print(person_dct)
#print(person_dct['name'])

# Change dictionary to json
person_json_converted = json.dumps(person_dct, indent=3)
print(type(person_json_converted))
print(person_json_converted)