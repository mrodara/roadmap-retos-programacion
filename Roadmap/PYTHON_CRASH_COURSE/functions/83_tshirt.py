"""
8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
text of a message that should be printed on the shirt. The function should print a
sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the
function a second time using keyword arguments.
"""

def make_shirt(size: str = "L", message: str = ""):
    print(f"You have ordered a shirt size: {size.upper()} with the message: {message}")

make_shirt("Xl", "Tonto el que lo lea")
make_shirt(message="Tu si que eres tonto", size="XS")