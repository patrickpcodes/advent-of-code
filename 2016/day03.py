from pathlib import Path

# Get the directory where this script is located
script_dir = Path(__file__).parent
input_path = script_dir / 'input03.txt'

with open(input_path, 'r') as f:
    text = f.read()

rows = text.split('\n')
rows = [r.strip() for r in rows]
rows = [
    (int(parts[0]), int(parts[1]), int(parts[2]))
    for parts in (r.strip().split() for r in rows)
]

count = 0

import itertools


def is_possible_triangle(sides):
    for t in itertools.permutations(sides):
        if t[0] + t[1] <= t[2]:
            return False
    return True

for row in rows:
    if is_possible_triangle(row):
        count+=1

print(count)

triangles = []
rows = text.split('\n')
rows = [r.strip() for r in rows]

for i in range(0, len(rows), 3):
    a = rows[i].split()
    b = rows[i+1].split()
    c = rows[i+2].split()

    for j in range(3):
        triangles.append((int(a[j]), int(b[j]), int(c[j])))

col_count = 0
for triangle in triangles:
    if is_possible_triangle(triangle):
        col_count+=1
print(col_count)