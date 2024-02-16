#Method Resolution Order

#Que ocurre cuando clases que heredan de otras tienen atributos y métodos iguales, ¿Cuales se llaman antes?
"""
Esto con la llamada a super() python se encarga de mirarlo y generalmente lo hace según el orden en
el que hayamos puesto las clases de las que se heredan.
"""

class A:
    def hablar(self):
        print("Hola desde A")

class B(A):
    def hablar(self):
        print("Hola desde B")

class C(A):
    def hablar(self):
        print("Hola desde C")

class D(B,C):
    #def hablar(self):
    #    print("Hola desde D")
    pass
d = D()

d.hablar()

print(D.mro())