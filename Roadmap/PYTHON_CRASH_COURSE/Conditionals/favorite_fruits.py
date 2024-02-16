favorite_fruits = ["mango", "pinapple", "watermelon", "pear"]

fruit = input("Introduce one of my favorite fruits: ")


if fruit.lower() in favorite_fruits:
    print(f"Yeah, you really like {fruit} !!!")
else:
    print("Sorry, you dont know me!!")