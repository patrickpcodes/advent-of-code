from pathlib import Path

# Get the directory where this script is located
script_dir = Path(__file__).parent
input_path = script_dir / 'input.txt'

with open(input_path, 'r') as f:
    text = f.read()


import re
rows = text.split("\n")

replacements = {}
replacements[r'\\"'] = 'a'
replacements[r'\\\\'] = 'a'
replacements[r'\\x([0-9A-Fa-f]{2})'] = 'a'

total_code = 0
total_cleaned = 0
for row in rows:
    total_code += len(row)
    row = row[1:-1]
    for key in replacements:
        row = re.sub(key, replacements[key], row)
    total_cleaned += len(row)

print(total_code)
print(total_cleaned)
print(total_code-total_cleaned)

rows = text.split("\n")
replacements = {}
replacements[r'\\"'] = 'aaaa'
replacements[r'\\\\'] = 'aaaa'
replacements[r'\\x([0-9A-Fa-f]{2})'] = 'aaaaa'

total_code = 0
total_encoded = 0
for row in rows:
    total_code += len(row)
    row = row[1:-1]
    for key in replacements:
        row = re.sub(key, replacements[key], row)
    total_encoded += len(row) + 6

print(total_code)
print(total_encoded)
print(total_encoded-total_code)