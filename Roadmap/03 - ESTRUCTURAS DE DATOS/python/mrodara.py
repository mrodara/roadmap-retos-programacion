##Estructuras de datos en Python
#
##Listas
#number_list = [1, 2, 3, 4, 5]
#
#char_list = ['a', 'b', 'c', 'd', 'e']
#
##Tuplas Tipo de dato inmutable
#number_tuple = (1, 2, 3, 4, 5)
#char_tuple = ('a', 'b', 'c', 'd', 'e')
#
##Diccionarios
#person1 = {
#    "name": "Miguel",
#    "surname": "Rodriguez",
#    "age": 27,
#    "phone": "1234567890",
#    "active": True
#}
#
#person2 = {
#    "name": "Pedro",
#    "surname": "Rodriguez",
#    "age": 44,
#    "phone": "666111333",
#    "active": False
#}
#
#notebook = [person1, person2]
#
#for person in notebook:
#    if "pedro" in person["name"].lower():
#        print("Pedro esta en el notebook")
#        break
#    else:
#        print("Pedro no esta en el notebook")
#
##if "Pedro" in notebook:
##    print("Pedro esta en el notebook")
##else:
##    print("Pedro no esta en el notebook")
#
##List Comprenhension
#my_string = "Hello world"
#mylist = [i for i in range(1, 11)]
#my_charlist = [i for i in my_string.lower() if i != " "]
#
#print(person1)
#print(mylist)
#print(my_charlist)
#
#sorted_charlist = sorted((my_charlist))
#print(sorted_charlist)
#
##Sorted list whitout duplicates
#sorted_charlist = sorted(set(my_charlist))
#print(sorted_charlist)
#

#List operations
#Append
#print(mylist.append(44))



def exists_contact(contact_list: list, phone: str) -> bool:
    for contact in contact_list:
        if contact["phone"] == phone:
            return True
    return False

def add_contact(contact_list: list, contact: dict):
    
    contact["name"] = input("Ingrese el nombre del contacto: ")
    contact["phone"] = input("Ingrese el numero del contacto: ")
    
    if len(contact_list) > 0:
        if exists_contact(contact_list, contact["phone"]):
            print("El numero de telefono ya existe")
        else:
            contact["email"] = input("Ingrese el email del contacto: ")
            add_contact(contact_list, contact)
    else:         
        contact["email"] = input("Ingrese el email del contacto: ")
        
def update_contact():
    contact["name"] = input("Ingrese el nombre del contacto: ")
    contact["phone"] = input("Ingrese el numero del contacto: ")
    contact["email"] = input("Ingrese el email del contacto: ")
    print("Contacto actualizado con exito")
    
def show_contacts(contact_list: list):
    if len(contact_list) == 0:
        print("No hay contactos para mostrar")
    else:
        print("-------------------------------")
        for contact in contact_list:
            print(f"Nombre: {contact['name']}")
            print(f"Telefono: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print("-------------------------------")

def delete_contact(contact_list: list, phone: str):
    if exists_contact(contact_list, phone):
        contact_list.remove(contact)
        print("Contacto eliminado con exito")

def show_menu():
    print("Bienvenido al gestor de contactos")
    print("1. Agregar contacto")
    print("2. Actualizar contacto")
    print("3. Eliminar contacto")
    print("4. Buscar contacto")
    print("5. Listar contactos")
    print("6. Salir")
    option = int(input("Ingrese la opcion deseada: "))
    return option

def search_contact(contact_list: list, phone: str):
    if exists_contact(contact_list, phone):
        print("-------------------------------")
        print(f"Nombre: {contact['name']}")
        print(f"Telefono: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print("-------------------------------")
    else:
        print("El contacto no existe")

contact_list = []
exit = False

while not exit:
    option = show_menu()
    contact = dict()
    if option == 1:
        add_contact(contact_list, contact)       
    elif option == 2:
        if exists_contact(contact_list, contact["phone"]):
            update_contact()
    elif option == 3:
        delete_contact(contact_list, input("Ingrese el numero del contacto: "))
    elif option == 4:     
        search_contact(contact_list, input("Ingrese el numero del contacto: "))
    elif option == 5:     
        show_contacts(contact_list)
    else:
        exit = True