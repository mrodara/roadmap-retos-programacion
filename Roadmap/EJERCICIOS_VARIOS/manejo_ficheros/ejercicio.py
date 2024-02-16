import os

#Current Path
current_dir = os.path.dirname(os.path.abspath(__file__))

#Current File
file_path = os.path.join(current_dir, 'files/personas.txt')

#Obtainig file lines to convert to dict
contacts = []

with open(file_path, "r", encoding="utf-8") as origin_file:
    lines = origin_file.read().splitlines()
    for line in lines:
        line_parsed = line.split(";")
        contact = {
            "id":       line_parsed[0],
            "name":     line_parsed[1],
            "surname":  line_parsed[2],
            "birthday": line_parsed[3]
        }