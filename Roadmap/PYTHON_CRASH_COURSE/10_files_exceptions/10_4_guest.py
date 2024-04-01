"""
10-4. Guest: Write a program that prompts the user for their name. When they
respond, write their name to a file called guest.txt.
"""

from pathlib import Path

file = Path('guest.txt')

name = input('Welcome, write your name: ')

file.write_text(name)