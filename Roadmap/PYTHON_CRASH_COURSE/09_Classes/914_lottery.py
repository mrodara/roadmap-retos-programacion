"""
9-14. Lottery: Make a list or tuple containing a series of 10 numbers and 5 letters.
Randomly select 4 numbers or letters from the list and print a message saying that
any ticket matching these 4 numbers or letters wins a prize.
"""
from random import randint

options = [1,2,3,4,5,6,7,8,9,10,'a','b','c','d','e']

selected = []

iteration = 0

while iteration < 4:
    position = randint(0,14)
    selected.append(options[position])
    iteration+=1

print(f'The winner serie is {selected}')