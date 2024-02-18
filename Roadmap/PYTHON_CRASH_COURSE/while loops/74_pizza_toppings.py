"""
7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
pizza toppings until they enter a 'quit' value. As they enter each topping, print
a message saying you’ll add that topping to their pizza.
"""

topping = ""

toppings = []

while topping.lower() != "quit":
    topping = input("Introduce the topping you desire: (quit for finish):")
    if topping.lower() == "quit":
        continue
    
    toppings.append(topping)
    print(f"I`ll add {topping} topping to your pizza...")
    
print("Preparing pizza...")

for topping in toppings:
    print(f"Adding {topping}")

print("Your pizza is finished, pay to the cashier please")