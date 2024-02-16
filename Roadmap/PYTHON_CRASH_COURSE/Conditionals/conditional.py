cars = ["audi", "bmw", "subaru", "toyota"]

for car in cars:
    if car.lower() == "bmw":
        print(f"This is my car: {car.upper()}")
    else:
        print(car.title())


#Pertenencia
print("bmw" in cars)

brand_car = "Renault"
print(brand_car.lower() not in cars)