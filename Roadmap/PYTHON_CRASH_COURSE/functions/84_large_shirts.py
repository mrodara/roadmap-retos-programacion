"""
8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python. Make a large shirt and a
medium shirt with the default message, and a shirt of any size with a different
message.
"""

def make_shirt(size: str = "L", message: str = "I love Python"):
    print(f"You have ordered a shirt size: {size.upper()} with the message: {message}")

make_shirt()
make_shirt("XXL", "Me too.")
