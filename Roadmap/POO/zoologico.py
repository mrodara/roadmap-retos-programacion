class Animal():
    def __init__(self, name, specie, age) -> None:
        self.name = name
        self.specie = specie
        self.age = age
    
    def comer(self):
        return f"Estoy comiendo un poco"
    
class Mamifero(Animal):
    def __init__(self, name, specie, age, legs, color="") -> None:
        super().__init__(name, specie, age)
        self.legs = legs
        self.color = color
    
    def amamantar(self):
        return f"Estoy dando el pecho..."

class Ave(Animal):
    def __init__(self, name, specie, age, size) -> None:
        super().__init__(name, specie, age)
        self.size = size
    
    def volar(self):
        return f"Estoy volando porque soy un ave"
    
class Murcielago(Mamifero, Ave):
    
    def __init__(self, name, specie, age, legs, color, size) -> None:
        Mamifero().__init__(name, specie, age, legs, color)
        Ave().__init__(size)
        

print(Murcielago.mro())