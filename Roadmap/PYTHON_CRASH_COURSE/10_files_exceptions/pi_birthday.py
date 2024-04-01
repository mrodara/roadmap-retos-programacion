from pathlib import Path

file = Path('./pi_million_digits.txt').resolve()

contents = file.read_text().splitlines()

pi_text = ''

for line in contents:
    pi_text += line.strip()


print('Is your birthday in pi number?')
birthday = input('Introduce your birthday in format ddmmyyyy')

if birthday in pi_text:
    print('Whooaaaa your birthday is in pi number!!!')
else:
    print("Nooooooo it isn't")