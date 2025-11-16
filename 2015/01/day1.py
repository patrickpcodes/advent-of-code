from pathlib import Path

# Get the directory where this script is located
script_dir = Path(__file__).parent
input_path = script_dir / 'input_1.txt'

with open(input_path, 'r') as f:
    text = f.read()

count = 0
for char in text:
    if char == '(':
        count += 1
    elif char == ')':
        count -= 1

print(count)
count = 0
index = -1
for char in text:
    index += 1
    if char == '(':
        count += 1
    elif char == ')':
        count -= 1
    if count == -1:
        break
print(index + 1)  # +1 to convert from 0-based to 1-based index