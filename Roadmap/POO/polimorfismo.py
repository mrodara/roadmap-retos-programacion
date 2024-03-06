class Gato():
    def sonido(self):
        return "Miau"

class Perro():
    def sonido(self):
        return "Guau"


#Otra manera de definir el polimorfismo es a través de una función que recibe un objeto
def hacer_sonido(animal: object) -> str:
    print(animal.sonido())

gato = Gato()
perro = Perro()

print(gato.sonido())
print(perro.sonido())

#Llamada a la función polimórfica:
hacer_sonido(gato)
hacer_sonido(perro)


'''
POLIMORFISMO EN LA HERENCIA
'''
class Mamifero():
    
    def amantar(self):
        pass
    
class Conejo(Mamifero):
    
    def amantar(self):
        return "Estoy amamantando"

conejo = Conejo()
print(conejo.amantar())