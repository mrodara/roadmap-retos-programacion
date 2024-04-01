"""
Read in each line from the file you just created, learning_python.txt, and
replace the word Python with the name of another language, such as C. Print
each modified line to the screen.
"""

from pathlib import Path

file = Path('./learning.txt').resolve()

contents = file.read_text().splitlines()

string = 'In Python you can learn:'

for line in contents:
    print(f' {string.replace('Python', 'PHP')} {line}')