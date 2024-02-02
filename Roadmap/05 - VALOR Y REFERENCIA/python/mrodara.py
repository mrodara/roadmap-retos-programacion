#Paso por valor
def doblar_valor(numero):
    numero*=2
    
n = 10 
doblar_valor(n)
print(n)

#Paso por referencia
def doblar_valores(numeros):
    for i,n in enumerate(numeros):
        numeros[i]*=2  

ns = [10,50,100]
doblar_valores(ns)
print(ns)


def interchange(a: int, b: int):
    new_a = b
    new_b = a
    
    return new_a, new_b

a = 10
b = 20
print(a, b)
a2, b2 = interchange(a, b)
print(a2, b2)

def new_interchange(numbers_a: list, numbers_b: list):
    new_numbers_a = numbers_b
    new_numbers_b = numbers_a
    
    return new_numbers_a, new_numbers_b

numbers_a = [1, 2, 3, 4, 5]
numbers_b = [6, 7, 8, 9, 10]
print(numbers_a, numbers_b)
numbers_a2, numbers_b2 = new_interchange(numbers_a, numbers_b)
print(numbers_a2, numbers_b2)
