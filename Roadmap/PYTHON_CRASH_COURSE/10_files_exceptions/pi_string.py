from pathlib import Path

path = Path('./pi_million_digits.txt').resolve()

content = path.read_text().splitlines()

pi_str = ''

for line in content:
    pi_str += line.lstrip()
    
print(f'{pi_str[:52]}')
print(f'{len(pi_str)}')