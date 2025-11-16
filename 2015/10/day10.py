from pathlib import Path

# Get the directory where this script is located
script_dir = Path(__file__).parent
input_path = script_dir / 'input.txt'

with open(input_path, 'r') as f:
    text = f.read()


import re
rows = text.split("\n")

puzzle = 3113322113

def apply(d):
    d = str(d)
    r = ""
    current_digit = 0
    current_count = 0
    for i in d:
        if i == current_digit:
            current_count += 1
        else:
            if current_count != 0:
                r += str(current_count)
                r += str(current_digit)
            current_digit = i
            current_count = 1
    if current_count != 0:
                r += str(current_count)
                r += str(current_digit)
    return r




res = puzzle
for i in range(40):
    res = apply(res)
    print(res)

print(len(res))
res = puzzle
for i in range(50):
    res = apply(res)
    print(res)

print(len(res))