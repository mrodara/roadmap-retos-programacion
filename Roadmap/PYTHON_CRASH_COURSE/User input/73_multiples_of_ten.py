"""
7-3. Multiples of Ten: Ask the user for a number, and then report whether the
number is a multiple of 10 or not.
"""

number = int(input("Introduce a number to ask: "))

if number % 10 == 0:
    print("The number is multiple of 10")
else:
    print("The number is not multiple of 10")