class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre #Usando __ indicamos a python que es un atributo muy privado para acceder requiere funciones getter y setter
        self.__edad = edad
    
    @property #De este modo podemos llamar a get_nombre como si fuese una propiedad, no necesita paréntesis
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    @property
    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        self.__edad = edad

# Crear una instancia de la clase Persona
persona = Persona("Juan", 25)

# Acceder a los atributos encapsulados
print(persona.get_nombre())  # Imprime "Juan"
print(persona.get_edad())  # Imprime 25

#Con el decorador
print(persona.get_nombre) # Imprime "Juan"

# Modificar los atributos encapsulados
persona.set_nombre("Pedro")
persona.set_edad(30)

print(persona.get_nombre())  # Imprime "Pedro"
print(persona.get_edad())  # Imprime 30