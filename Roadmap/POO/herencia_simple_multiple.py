class Persona:
    def __init__(self, name: str, age: int, email: str):
        self.name = name
        self.age = age
        self.email = email
    
    @property
    def get_name(self) -> str:
        return "Hola me llamo " + self.name
    
    def set_name(self, name: str):
        self.name = name
    
    def hablar(self):
        print("Charlemos un poco")

class Artista:
    def __init__(self, hability: str = "") -> None:
        self.hability = hability
    
    @property
    def get_hability(self):
        if self.hability != "":
            return f"Mi habilidad es {self.hability}"
        return f"No tengo habilidad definida..."
    
class Estudiante(Persona):
    def __init__(self, name: str, age: int, email: str, subjects: list = []):
        super().__init__(name, age, email)
        self.subjects = subjects

#Ejemplo de herencia múltiple
class PersonArtist(Persona, Artista):
    def __init__(self, name: str, age: int, email: str, hability: str, cache: float = 0):
        Persona.__init__(self, name, age, email) #En lugar de indicar super decimos la clase de la que hereda
        Artista.__init__(self, hability)
        self.cache = cache
    
    @property
    def get_cache(self):
        return f"Actualmente mi cache es de: ${self.cache} "
        

    def set_cache(self, cache: float):
        if cache > 0:
            self.cache = cache
            print("Se ha actualizado el caché del artista")
        else:
            print("Debes introducir un valor decimal que sea mayor que 0.")
            
    def introduce_yourself(self):
        return f"Hola me llamo {self.name}, actualmente {Artista().get_hability} y por ello {self.get_cache}"

        
student = Estudiante("Manuel", 44, "mjrodriguezarabi@gmail.com", ['SRI', 'PIA'])
person_artist = PersonArtist("Virgilio", 100, "virgi100@gmail.com", "Saco mocos como estalactitas", 10000.34)


#print(student.get_name)
#student.hablar()

print(person_artist.get_name)
print(person_artist.get_hability)
person_artist.set_cache(-100)
person_artist.set_cache(12000.45)
print(person_artist.get_cache)
print(person_artist.introduce_yourself())
