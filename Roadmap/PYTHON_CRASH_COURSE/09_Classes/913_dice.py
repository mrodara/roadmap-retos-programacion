"""
9-13. Dice: Make a class Die with one attribute called sides, which has a
default value of 6. Write a method called roll_die() that prints a random num-
ber between 1 and the number of sides the die has. Make a 6-sided die and
roll it 10 times.
"""
from random import randint

class Dice:
    def __init__(self, sides: int = 6):
        self.sides = sides
        
    def roll_dice(self):
        return randint(1, self.sides)
    
my_dice = Dice()

for value in range(1,11):
    print(my_dice.roll_dice())

dice2 = Dice(sides=10)

for value in range(1,11):
    print(dice2.roll_dice())

