
from pathlib import Path

# Get the directory where this script is located
script_dir = Path(__file__).parent
input_path = script_dir / 'input04.txt'

with open(input_path, 'r') as f:
    text = f.read()



rows = text.split("\n")

grid = []

for r in rows:
    row = []
    for c in r:
        row.append(c)
    grid.append(row)

print(grid)

count = 0

def can_be_accessed(x, y, grid, num):
    count = 0
    if grid[x][y] != "@":
        return False
    move = [-1, 0, 1]
    for m in move:
        for n in move:
            if m == 0 and n ==0:
                continue
            if x + m >= 0 and x + m < len(grid):
                if y + n >= 0 and y + n < len(grid[0]):
                    count += 1 if grid[x + m][y + n] == "@" else 0

    return count < num

for i in range(len(grid)):
    for j in range(len(grid[0])):
        count += 1 if can_be_accessed(i, j, grid, 4) else 0
print(count)

# with remove
overall_count = 0
while True:
    current_count = 0
    cells_to_remove = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if can_be_accessed(i, j, grid, 4):
                current_count +=1
                cells_to_remove.append((i, j))
    overall_count += current_count
    if len(cells_to_remove) == 0:
        break
    else:
        for x in cells_to_remove:
            grid[x[0]][x[1]] = "."


print(overall_count)
