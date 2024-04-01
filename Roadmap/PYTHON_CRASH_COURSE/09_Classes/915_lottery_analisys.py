"""
9-15. Lottery Analysis: You can use a loop to see how hard it might be to win
the kind of lottery you just modeled. Make a list or tuple called my_ticket. Write

a loop that keeps pulling numbers until your ticket wins. Print a message report-
ing how many times the loop had to run to give you a winning ticket.
"""

from random import randint

my_ticket = [5,7,9,'a','c']
my_ticket = [str(i) for i in my_ticket] #Convierto números a cadena para poder ordenarlos
sorted_ticket = sorted(my_ticket)
options = [1,2,3,4,5,6,7,8,9,10,'a','b','c','d','e']
options = [str(i) for i in options]

def get_lottery(options: list):

    selected = []

    iteration = 0

    while iteration < 5:
        position = randint(0,14)
        selected.append(options[position])
        iteration+=1
    
    selected_sorted = sorted(selected)
    return selected_sorted

# times to win
times = 0
print('Start combinations')
win_combination = get_lottery(options=options)
while not my_ticket == win_combination: 
    times+=1
    print(f'{times} - {win_combination}')
    win_combination = get_lottery(options=options)
    
print(f'Congrats, you have win lottery after {times} times raffles')

