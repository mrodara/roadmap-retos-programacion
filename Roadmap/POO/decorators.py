def decorador(funcion):
    def funcion_modificada():
        print("Antes de llmar a la función")
        funcion()
        print("Después de llamar a la función")
    return funcion_modificada()

# def saludo():
#     print("Hola soy Manu")
    
# saludo_modificado = decorador(saludo)

@decorador
def saludo():
    print("Hola Soy Manu")