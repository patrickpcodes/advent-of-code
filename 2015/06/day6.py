from pathlib import Path

# Get the directory where this script is located
script_dir = Path(__file__).parent
input_path = script_dir / 'input.txt'

with open(input_path, 'r') as f:
    text = f.read()


from re import search
rows = text.split("\n")

import numpy as np
grid = np.zeros((1000, 1000), 'int32')

data = [d.split(' ') for d in rows]

for row_data in data:
    if row_data[0] == "turn":
        x1, y1 = row_data[2].split(",")
        x2, y2 = row_data[4].split(",")
        x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
        if row_data[1] == "on":
            grid[x1:x2+1, y1:y2+1] = 1
        else:
            assert row_data[1] == "off"
            grid[x1:x2+1, y1:y2+1] = 0
    else:
        x1, y1 = row_data[1].split(',')
        x2, y2 = row_data[3].split(',')
        x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
        grid[x1:x2+1, y1:y2+1] = np.logical_not(grid[x1:x2+1, y1:y2+1])
    print(np.sum(grid))

print("Part 1")
print(np.sum(grid))

grid = np.zeros((1000, 1000), 'int32')

data = [d.split(' ') for d in rows]

for row_data in data:
    if row_data[0] == "turn":
        x1, y1 = row_data[2].split(",")
        x2, y2 = row_data[4].split(",")
        x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
        if row_data[1] == "on":
            grid[x1:x2+1, y1:y2+1] += 1
        else:
            assert row_data[1] == "off"
            grid[x1:x2+1, y1:y2+1] -= 1
            grid[grid < 0] = 0
    else:
        x1, y1 = row_data[1].split(',')
        x2, y2 = row_data[3].split(',')
        x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
        grid[x1:x2+1, y1:y2+1] += 2
    print(np.sum(grid))
print("Part 2")
print(np.sum(grid))

x = 123
y = 456
print("And")
print(x & y)