"""
10-5. Guest Book: Write a while loop that prompts users for their name. Collect
all the names that are entered, and then write these names to a file called
guest_book.txt. Make sure each entry appears on a new line in the file.
"""

from pathlib import Path

file = Path('guestbook.txt')

exit = False
names = ""

while not exit:
    name = input('Introduce your name or exit to quit: ')
    
    if name.lower() == 'exit':
        exit = True
        break
    
    names += name + '\n'

file.write_text(names)
     