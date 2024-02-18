"""
7-10. Dream Vacation: Write a program that polls users about their dream vaca-
tion. Write a prompt similar to If you could visit one place in the world, where
would you go? Include a block of code that prints the results of the poll.
"""

active = True

poll_answers = {}

while active:
    name = input("What`s your name?: ")
    
    while not name:
        print("You should input your name for the poll")
        name = input("What`s your name?: ")
    
    place = input("If you could visit one place in the world, where would you go?: ")
    
    poll_answers[name] = place
    
    repeat = input("There is another person to the poll? (y/n): ")
    
    if repeat.lower() == 'n':
        active = False

print("Poll results:")

for name, place in poll_answers.items():
    print(f"{name.title()} would like to go to {place.title()}")