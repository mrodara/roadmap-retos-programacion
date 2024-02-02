def area_polygon(type_polygon: str):
    
    area = 0
    
    if type_polygon.lower() == "triangulo":
        b = float(input("Introduce la longitud de la base: "))
        h = float(input("Introduce la longitud de la altura: "))
        
        while not b or not(b != 0):
            b = float(input("Introduce la longitud de la base: "))
        
        while not h or not(h != 0):
            h = float(input("Introduce la longitud de la altura: "))
        
        area = (b*h) / 2
    
    elif type_polygon.lower() == "cuadrado":
        side = float(input("Introduce la longitud del lado del cuadrado: "))
        
        while not side or side == 0:
            side = float(input("Introduce la longitud del lado del cuadrado: "))
        
        area = side*2
    
    elif type_polygon.lower() == "rectangulo":
        
        longitude = float(input("Introduzca la longitud del rectángulo: "))
        
        while not longitude:
            longitude = float(input("Introduzca la longitud del rectángulo: "))
        
        width = float(input("Introduzca la anchura del rectángulo: "))
        
        while not width:
            width = float(input("Introduzca la anchura del rectángulo: "))
        
        area = longitude * width
    
    else:
        return -1

    return area

my_area1 = area_polygon("triangulo")
print(f"El area del Triángulo es: {my_area1}")
my_area2 = area_polygon("CUADRADO")
print(f"El area del Cuadrado es: {my_area2}")
my_area3 = area_polygon("Rectangulo")
print(f"El area del Rectángulo es: {my_area3}")

print(area_polygon("Pentágono"))