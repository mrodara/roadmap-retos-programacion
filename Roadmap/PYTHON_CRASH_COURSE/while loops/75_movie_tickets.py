"""
7-5. Movie Tickets: A movie theater charges different ticket prices depending on
a person’s age. If a person is under the age of 3, the ticket is free; if they are
between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
$15. Write a loop in which you ask users their age, and then tell them the cost
of their movie ticket.
"""

age = 0

while age != 999:
    age = int(input("Introduce the person`s age (999 to quit): "))
    if age >= 0 and age < 3:
        print("The ticket is free...")
    elif age >= 3 and age <= 12:
        print("The ticket is $10...")
    elif age > 12 and age != 999:
        print("The ticket is S15")
    else:
        continue
print("Program end")