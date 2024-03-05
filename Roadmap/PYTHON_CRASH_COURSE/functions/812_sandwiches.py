"""
8-12. Sandwiches: Write a function that accepts a list of items a person wants
on a sandwich. The function should have one parameter that collects as many
items as the function call provides, and it should print a summary of the sand-
wich that’s being ordered. Call the function three times, using a different num-
ber of arguments each time.
"""

def items_sandwich(*items):
    print("Sumarizing your sanchwich ingredients: ")
    for item in items:
        print(f"adding {item}")
    print("Your sandwich is ready, grab it and enjoy")

items_sandwich('tomato', 'lettuce', 'tuna')
items_sandwich('tomato', 'lettuce', 'tuna', 'bacon', 'mayo chipotle')
items_sandwich('tomato', 'lettuce', 'tuna', 'spicy cheese', 'chicken')