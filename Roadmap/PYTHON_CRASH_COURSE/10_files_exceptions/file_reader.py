from pathlib import Path

current_path = Path('pi.txt')

my_path = current_path.resolve()

contents = my_path.read_text().rstrip()
#contents = contents.rstrip()

print(contents)
