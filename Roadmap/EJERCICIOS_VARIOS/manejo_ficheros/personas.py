import os

# Obtén la ruta del directorio actual
current_dir = os.path.dirname(os.path.abspath(__file__))

# Añade el nombre del archivo a la ruta del directorio
file_path = os.path.join(current_dir, "personas.txt")

contacts = []

if os.path.isfile(file_path):
    with open(file_path, "r", encoding="utf-8") as my_file:
        for person in my_file.readlines():
            person = person.strip()
            contact = {
                "id":       person.split(";")[0],
                "name":     person.split(";")[1],
                "surname":  person.split(";")[2],
                "birthday": person.split(";")[3],
            }
            
            contacts.append(contact)            
else:
    print("El archivo personas.txt no se encuentra en el directorio actual.")
    
print(contacts)