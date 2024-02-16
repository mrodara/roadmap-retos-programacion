import os

#Current Path
current_dir = os.path.dirname(os.path.abspath(__file__))

#Current File
file_path = os.path.join(current_dir, 'files/personas.txt')

#print(file_path)

with open(file_path, "r") as file:
    #text = file.read()
    #print(type(text))
    #print(text)
    #lines = file.readlines()
    #for line in lines:
    #    print(line)
    lines = file.read().splitlines()
    #print(lines)
    
    print("#####################")
    for line in lines:
        person = line.split(";")
        print(f"Id: {person[0]}")
        print(f"Name: {person[1]}")
        print(f"Surname: {person[2]}")
        print(f"Birthday: {person[3]}")
        print("#####################")