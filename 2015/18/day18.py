from pathlib import Path

# Get the directory where this script is located
script_dir = Path(__file__).parent
input_path = script_dir / 'input.txt'

with open(input_path, 'r') as f:
    text = f.read()

rows = text.split('\n')
grid = []
for row in rows:
    grid.append(list(row))

# print(grid)

def get_on_neighbors(grid, check_vals):
    count = 0
    for val in check_vals:
        if grid[val[0]][val[1]] == "#":
            count += 1
    return count


def get_next_state(i, j, grid):
    check_vals = []
    on = grid[i][j] == "#"
    if (i==0 and j == 0) or (i ==0 and j == 99) or (i == 99 and j == 0 ) or (i == 99 and j == 99):
        return "#"
    if i - 1 >= 0 and j - 1 >= 0:
        check_vals.append((i-1, j-1))
    if i - 1 >= 0:
        check_vals.append((i-1, j))
    if i - 1 >= 0 and j + 1 < len(grid[i]):
        check_vals.append((i-1, j+1))
    if j - 1 >= 0:
        check_vals.append((i, j-1))
    if j + 1 < len(grid[i]):
        check_vals.append((i, j+1))
    if i + 1 < len(grid) and j - 1 >= 0:
        check_vals.append((i+1, j-1))
    if i + 1 < len(grid):
        check_vals.append((i+1, j))
    if i + 1 < len(grid) and j + 1 < len(grid[i]):
        check_vals.append((i+1, j+1))
    on_neighbors = get_on_neighbors(grid, check_vals)
    next_state = "."
    if on:
        if on_neighbors == 2 or on_neighbors == 3:
            next_state = "#"
        else:
            next_state = "."
    else:
        if on_neighbors == 3:
            next_state = "#"
    return next_state

def get_next_grid(grid):
    next_grid = [[0 for _ in range(100)] for _ in range(100)]

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            next_grid[i][j] = get_next_state(i, j, grid)

    return next_grid

def print_grid(grid):
    s = ""
    for i in grid:
        for j in i:
            s+=j
        s+="\n"
    print(s)
num = 0
for i in grid:
    for j in i:
        if j == "#": num += 1

print(num)
print_grid(grid)
for i in range(100):
    grid = get_next_grid(grid)
    print_grid(grid)
    num = 0
    for i in grid:
        for j in i:
            if j == "#": num += 1

    print(num)

# Getting the final count
num = 0
for i in grid:
    for j in i:
        if j == "#": num += 1

print(num)
